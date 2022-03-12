from uuid import uuid4
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column,
    DateTime,
    String,
    Boolean,
    ForeignKey,
)
from app.db import Base
from sqlalchemy.orm import relationship


class User(Base):
    """
    Database model for an application user
    """

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    full_name = Column(String(255), index = True)
    phone_number = Column(String(13), unique=True, index=True, nullable=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean(), default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=True)
    user_role = relationship("UserRole", back_populates="user", uselist=False)
    account = relationship("Account", back_populates="users")

    def get_role(self) -> str:
        return self.user_role.role.name if self.user_role else "GUEST"