from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Any
from jose import jwt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"
class AuthManager:
    def __init__(self, token_expiry_minutes: int, secret_key: str):
        self.token_expiry_minutes = token_expiry_minutes
        self.secret_key = secret_key

    def create_access_token(self, subject: Any, expires_delta: timedelta = None):
        expire = datetime.utcnow()
        if expires_delta:
            expire += expires_delta
        else:
            expire += timedelta(minutes= self.token_expiry_minutes)

        to_encode = {"exp": expire, **subject}
        return jwt.encode(to_encode, self.secret_key, algorithm=ALGORITHM)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(plain_password: str) -> str:
        return pwd_context.hash(plain_password)