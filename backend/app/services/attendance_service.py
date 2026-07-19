import numpy as np
from app.ai.pipeline import FaceRecognitionPipeline, FaceTrack
from app.schemas.schemas import AttendanceCandidate, AttendancePreview

class AttendanceService:
    def __init__(self, pipeline: FaceRecognitionPipeline):
        self.pipeline = pipeline

    def build_preview(self, section_student_ids: list[str], tracks: list[FaceTrack], embeddings: dict[str, list[np.ndarray]]) -> AttendancePreview:
        matches = self.pipeline.match_tracks(tracks, embeddings)
        present_ids = {match.student_id for match in matches if match.student_id}
        present = [AttendanceCandidate(student_id=m.student_id, confidence=m.confidence, status="present", face_track_id=m.track_id) for m in matches if m.student_id]
        unknown = [AttendanceCandidate(student_id=None, confidence=m.confidence, status="unknown" if m.is_live else "rejected_liveness", face_track_id=m.track_id) for m in matches if not m.student_id]
        absent = [student_id for student_id in section_student_ids if student_id not in present_ids]
        return AttendancePreview(present=present, absent_student_ids=absent, unknown=unknown)
