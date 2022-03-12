from datetime import datetime
from uuid import uuid4

from app.db import Base
from sqlalchemy import Boolean, Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Account(Base):
    __tablename__="accounts"
    id = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid4
    )
    name = Column(String(255), index=True, nullable=False)
    description = Column(Text)
    is_active = Column(Boolean(), default=True)
    # plan_id = Column(UUID(as_uuid=True), index=True)
    # current_subscription_ends = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    
    users = relationship("User", back_populates="account")