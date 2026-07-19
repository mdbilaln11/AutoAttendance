from fastapi import APIRouter, Depends, UploadFile, File, Form
from app.ai.pipeline import FaceRecognitionPipeline
from app.core.config import get_settings
from app.schemas.schemas import AttendancePreview
from app.services.attendance_service import AttendanceService

router = APIRouter(prefix="/attendance", tags=["attendance"])

@router.post("/preview", response_model=AttendancePreview)
async def preview_attendance(
    department: str = Form(...),
    year: int = Form(...),
    section: str = Form(...),
    subject: str = Form(...),
    video: UploadFile = File(...),
):
    """Receive a classroom video and return teacher-verifiable attendance candidates.

    The endpoint is wired for the AI service boundary; production deployments should enqueue
    large videos to workers and persist source media to private object storage.
    """
    await video.read()
    service = AttendanceService(FaceRecognitionPipeline(get_settings().face_match_threshold))
    return service.build_preview(section_student_ids=[], tracks=[], embeddings={})
