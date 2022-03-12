from .base import DBCrud
from sqlalchemy.orm import Session
from typing import Optional, List, Any, Union
from pydantic import UUID4
from app import schemas, models


class UserRoleCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.UserRole
        self.model = models.UserRole

    def create(self, user_role: schemas.UserRoleCreate) -> models.UserRole:
        return self.save(self.model(user_id=user_role.user_id, role_id=user_role.role_id))

    def get_by_id(self, user_id: Union[str, UUID4]) -> Optional[models.UserRole]:
        return self.db.query(self.model).filter(self.model.user_id == user_id).first()

    def get_by_role_id(self, role_id: UUID4, limit: int=0) -> Optional[models.UserRole]:
        return self.db.query(self.model).filter(self.model.role_id == role_id).limit(limit).all()

    def get_all(self, limit: int = 0) -> List[models.UserRole]:
        return super().get_all(limit)

    def delete_by_id(self, user_id: Union[str, int]) -> models.UserRole:
        return self.db.query(self.model).filter(self.model.user_id == user_id).delete()

    def delete_by_role_id(self, role_id: str) -> Any:
        return self.db.query(self.model).filter(self.model.role_id == role_id).delete()

    def update(self, id: str) -> models.UserRole:
        return None