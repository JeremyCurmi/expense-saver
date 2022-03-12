from sqlalchemy.orm import Session
from app import models, schemas
from typing import List, Optional,Any
from datetime import datetime
from .base import DBCrud


class ProductCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.Product

    def create(self, *args, **kwargs) -> models.Product:
        return super().create(*args, **kwargs)

    def get_by_id(self, id: int) -> Optional[models.Product]:
        return super().get_by_id(id)

    def get_by_name(self, name: str) -> Optional[models.Product]:
        return self.db.query(self.model).filter(self.model.name == name).first()

    def get_all(self, limit: int = 0) -> List[models.Product]:
        return super().get_all(limit)

    def delete_by_id(self, id: int) -> models.Product:
        return super().delete_by_id(id)

    def delete_by_name(self, name: str) -> Any:
        return self.db.query(self.model).filter(self.model.name == name).delete()

    def update(self, id: int, product: schemas.ProductCreate) -> models.Product:
        product.updated_at = datetime.utcnow()
        return super().update(id, product.dict())
