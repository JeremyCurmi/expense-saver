from .base import DBCrud
from sqlalchemy.orm import Session
from typing import Optional, List, Any, Union
from pydantic import UUID4
from app import schemas, models

class RoleCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.Role

    def create(self, role: schemas.RoleCreate) -> models.Role:
        return self.save(self.model(name=role.name, description=role.description))

    def get_by_id(self, id: Union[str, UUID4]) -> Optional[models.Role]:
        return super().get_by_id(id)

    def get_by_name(self, name: str) -> Optional[models.Role]:
        return self.db.query(self.model).filter(self.model.name == name).first()

    def get_all(self, limit: int = 0) -> List[models.Role]:
        return super().get_all(limit)

    def delete_by_id(self, id: Union[str, int]) -> models.Role:
        return super().delete_by_id(id)

    def delete_by_name(self, name: str) -> Any:
        return self.db.query(self.model).filter(self.model.name == name).delete()

    def update(self, id: str) -> models.Role:
        return None