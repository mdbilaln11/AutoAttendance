from datetime import datetime, timedelta, timezone
from enum import StrEnum
from typing import Iterable
from jose import jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from app.core.config import get_settings

class Role(StrEnum):
    admin = "admin"
    principal = "principal"
    hod = "hod"
    teacher = "teacher"
    student = "student"

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)

def create_access_token(subject: str, role: Role) -> str:
    settings = get_settings()
    now = datetime.now(timezone.utc)
    payload = {"sub": subject, "role": role.value, "iat": now, "exp": now + timedelta(minutes=settings.access_token_expire_minutes)}
    return jwt.encode(payload, settings.secret_key, algorithm="HS256")

def assert_role(actual: Role, allowed: Iterable[Role]) -> None:
    if actual not in set(allowed):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
