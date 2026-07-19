from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class FaceTrack:
    track_id: str
    embedding: np.ndarray
    quality_score: float
    liveness_score: float

@dataclass(frozen=True)
class MatchResult:
    student_id: str | None
    confidence: float
    track_id: str
    is_live: bool

class FaceRecognitionPipeline:
    """Production integration point for detection, tracking, liveness, embeddings, and matching.

    The class is dependency-injection friendly so deployments can wire InsightFace, GPU workers,
    cloud storage, and vector indexes without changing API handlers.
    """

    def __init__(self, match_threshold: float = 0.72, liveness_threshold: float = 0.65):
        self.match_threshold = match_threshold
        self.liveness_threshold = liveness_threshold

    def cosine_similarity(self, left: np.ndarray, right: np.ndarray) -> float:
        denominator = np.linalg.norm(left) * np.linalg.norm(right)
        if denominator == 0:
            return 0.0
        return float(np.dot(left, right) / denominator)

    def match_tracks(self, tracks: list[FaceTrack], known_embeddings: dict[str, list[np.ndarray]]) -> list[MatchResult]:
        results: list[MatchResult] = []
        claimed_students: set[str] = set()
        for track in sorted(tracks, key=lambda item: item.quality_score, reverse=True):
            best_student: str | None = None
            best_score = 0.0
            for student_id, embeddings in known_embeddings.items():
                if student_id in claimed_students:
                    continue
                score = max((self.cosine_similarity(track.embedding, known) for known in embeddings), default=0.0)
                if score > best_score:
                    best_student, best_score = student_id, score
            is_live = track.liveness_score >= self.liveness_threshold
            if best_student and best_score >= self.match_threshold and is_live:
                claimed_students.add(best_student)
                results.append(MatchResult(best_student, best_score, track.track_id, True))
            else:
                results.append(MatchResult(None, best_score, track.track_id, is_live))
        return results
