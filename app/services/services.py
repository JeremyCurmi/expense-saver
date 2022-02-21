from abc import ABC, abstractmethod
from typing import List, Optional

from app import models, structs
from sqlalchemy.orm import Session


class DBCrud(ABC):
    model: models.Base
    db: Session

    def save(self, obj: models.Base) -> models.Base:
        self.db.add(obj)
        self.db.commit()
        return obj

    def save_all(self, objs: List[models.Base]):
        self.db.add_all(objs)
        self.db.commit()

    @abstractmethod
    def create(self, *args, **kwargs) -> models.Base:
        return self.save(self.model(*args, **kwargs))

    @abstractmethod
    def get_by_id(self, id: int) -> models.Base:
        return self.db.query(self.model).filter(self.model.id == id).first()

    @abstractmethod
    def get_all(self, limit: int = 0) -> List[models.Base]:
        if limit:
            return self.db.query(self.model).limit(limit).all()
        else:
            return self.db.query(self.model).all()


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

    def get_by_name(self, name: str) -> Optional[models.Shop]:
        return self.db.query(self.model).filter(self.model.name == name).first()

    def get_all(self, limit: int = 0) -> List[models.Category]:
        return super().get_all(limit)


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
