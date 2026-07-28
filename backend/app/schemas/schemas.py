from pydantic import BaseModel, EmailStr, Field

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class StudentCreate(BaseModel):
    name: str
    roll_number: str
    register_number: str
    department: str
    course: str
    semester: int
    year: int
    section: str
    email: EmailStr
    phone_number: str

class StudentRead(StudentCreate):
    id: str

class AttendanceCandidate(BaseModel):
    student_id: str | None
    name: str | None = None
    confidence: float
    status: str
    face_track_id: str

class AttendancePreview(BaseModel):
    present: list[AttendanceCandidate]
    absent_student_ids: list[str]
    unknown: list[AttendanceCandidate]
