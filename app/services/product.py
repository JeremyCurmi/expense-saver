from typing import List

from app import models, structs
from sqlalchemy.orm import Session


def get_product_by_id(db: Session, product_id: int) -> models.Product:
    return db.query(models.Product).filter(models.Product.id == product_id).first()


def get_product_by_name(db: Session, product_name: str) -> models.Product:
    return db.query(models.Product).filter(models.Product.name == product_name).first()


def get_products(db: Session, skip: int = 0, limit: int = 100) -> List[models.Product]:
    return db.query(models.Product).offset(skip).limit(limit).all()
