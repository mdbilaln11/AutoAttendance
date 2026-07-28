import numpy as np
from app.ai.pipeline import FaceRecognitionPipeline, FaceTrack

def test_pipeline_matches_once_and_rejects_duplicate_identity():
    pipeline = FaceRecognitionPipeline(match_threshold=0.8)
    known = {"student-1": [np.array([1.0, 0.0])], "student-2": [np.array([0.0, 1.0])]}
    tracks = [FaceTrack("a", np.array([0.99, 0.01]), 0.9, 0.9), FaceTrack("b", np.array([0.98, 0.02]), 0.8, 0.9)]
    results = pipeline.match_tracks(tracks, known)
    assert [item.student_id for item in results].count("student-1") == 1
    assert any(item.student_id is None for item in results)
