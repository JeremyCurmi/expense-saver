from typing import List, Optional

from app import models, schemas
from sqlalchemy.orm import Session
from .base import DBCrud

class ShopCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.Shop

    def create(self, *args, **kwargs) -> models.Shop:
        return super().create(*args, **kwargs)

    def get_by_id(self, id: int) -> Optional[models.Shop]:
        return super().get_by_id(id)

    def get_by_name(self, name: str) -> Optional[models.Shop]:
        return self.db.query(self.model).filter(self.model.name == name).first()

    def get_all(self, limit: int = 0) -> List[models.Shop]:
        return super().get_all(limit)


class ProductShopsCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.ProductShop

    def create(self, *args, **kwargs) -> models.ProductShop:
        return super().create(*args, **kwargs)

    def get_by_id(self) -> models.Base:
        return None

    def get_all(self, limit: int = 0) -> List[models.ProductShop]:
        return super().get_all(limit)

    def get_by_product_id(self, product_id: int) -> List[models.ProductShop]:
        return (
            self.db.query(self.model).filter(self.model.product_id == product_id).all()
        )

    def get_by_shop_id(self, shop_id: int) -> List[models.ProductShop]:
        return self.db.query(self.model).filter(self.model.shop_id == shop_id).all()


class CategoryCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.Category

    def create(self, *args, **kwargs) -> models.Category:
        return super().create(*args, **kwargs)

    def get_by_id(self, id: int) -> Optional[models.Category]:
        return super().get_by_id(id)

    def get_by_name(self, name: str) -> Optional[models.Category]:
        return self.db.query(self.model).filter(self.model.name == name).first()

    def delete_by_id(self, id: int) -> models.Product:
        return super().delete_by_id(id)

    def get_all(self, limit: int = 0) -> List[models.Category]:
        return super().get_all(limit)

    def update(self, id: int, category: schemas.CategoryCreate) -> models.Category:
        return super().update(id, category.dict())


class ProductCategoryCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.ProductCategory

    def create(self, *args, **kwargs) -> models.ProductCategory:
        return super().create(*args, **kwargs)

    def get_by_id(self) -> models.Base:
        return None

    def get_all(self, limit: int = 0) -> List[models.ProductCategory]:
        return super().get_all(limit)

    def get_by_product_id(self, product_id: int) -> List[models.ProductCategory]:
        return (
            self.db.query(self.model).filter(self.model.product_id == product_id).all()
        )

    def get_by_category_id(self, category_id: int) -> List[models.ProductCategory]:
        return (
            self.db.query(self.model)
            .filter(self.model.category_id == category_id)
            .all()
        )


class QuantityCrud(DBCrud):
    def __init__(self, db: Session):
        self.db = db
        self.model = models.Quantity

    def create(self, *args, **kwargs) -> models.Quantity:
        return super().create(*args, **kwargs)

    def get_by_id(self, id: int) -> Optional[models.Quantity]:
        return super().get_by_id(id)

    def get_by_name(self, name: str) -> Optional[models.Quantity]:
        return self.db.query(self.model).filter(self.model.name == name).first()

    def get_all(self, limit: int = 0) -> List[models.Quantity]:
        return super().get_all(limit)
