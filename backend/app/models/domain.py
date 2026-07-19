import uuid
from datetime import datetime
from sqlalchemy import DateTime, Enum, Float, ForeignKey, LargeBinary, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.security import Role
from app.db.session import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)
    role: Mapped[Role] = mapped_column(Enum(Role), index=True)
    is_active: Mapped[bool] = mapped_column(default=True)

class Student(Base):
    __tablename__ = "students"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String, index=True)
    roll_number: Mapped[str] = mapped_column(String, index=True)
    register_number: Mapped[str] = mapped_column(String, unique=True, index=True)
    department: Mapped[str] = mapped_column(String, index=True)
    course: Mapped[str] = mapped_column(String)
    semester: Mapped[int]
    year: Mapped[int]
    section: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String)
    embeddings: Mapped[list["FaceEmbedding"]] = relationship(back_populates="student")

class FaceEmbedding(Base):
    __tablename__ = "face_embeddings"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id: Mapped[str] = mapped_column(ForeignKey("students.id"), index=True)
    embedding: Mapped[bytes] = mapped_column(LargeBinary)
    pose: Mapped[str] = mapped_column(String)
    quality_score: Mapped[float] = mapped_column(Float)
    student: Mapped[Student] = relationship(back_populates="embeddings")

class AttendanceRecord(Base):
    __tablename__ = "attendance_records"
    __table_args__ = (UniqueConstraint("student_id", "subject", "attendance_date", name="uq_student_subject_date"),)
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id: Mapped[str] = mapped_column(ForeignKey("students.id"), index=True)
    teacher_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)
    subject: Mapped[str] = mapped_column(String, index=True)
    department: Mapped[str] = mapped_column(String, index=True)
    semester: Mapped[int]
    section: Mapped[str] = mapped_column(String, index=True)
    attendance_date: Mapped[str] = mapped_column(String, index=True)
    status: Mapped[str] = mapped_column(String)
    recognition_confidence: Mapped[float] = mapped_column(Float, default=0.0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    actor_id: Mapped[str] = mapped_column(String, index=True)
    action: Mapped[str] = mapped_column(String, index=True)
    entity_type: Mapped[str] = mapped_column(String)
    entity_id: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
