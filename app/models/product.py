from datetime import datetime

from app.core.db import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_modified = Column(DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name={self.name}, last_modified={self.last_modified})"
