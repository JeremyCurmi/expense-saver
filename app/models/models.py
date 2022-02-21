from datetime import datetime
from enum import Enum

from app.core.db import Base
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(200), nullable=True)
    updated_at = Column(DateTime, default=datetime.now())
    shops = relationship("Shop", secondary="product_shops", back_populates="products")
    categories = relationship(
        "Category", secondary="product_categories", back_populates="products"
    )

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name={self.name}, updated_at={self.updated_at})"


class Shop(Base):
    __tablename__ = "shops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    products = relationship(
        "Product", secondary="product_shops", back_populates="shops"
    )

    def __repr__(self) -> str:
        return f"Shop(name={self.name})"


class ProductShop(Base):
    __tablename__ = "product_shops"
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    shop_id = Column(Integer, ForeignKey("shops.id"), primary_key=True)
    price = Column(Float, nullable=False)

    PrimaryKeyConstraint("product_id", "shop_id")

    def __repr__(self) -> str:
        return f"ProductShop(product_id={self.product_id}, shop_id={self.shop_id})"


class CategoryType(Enum):
    # TODO: add more categories
    food = 1
    drink = 2
    other = 3


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(ChoiceType(CategoryType, impl=Integer()), nullable=False, unique=True)
    products = relationship(
        "Product", secondary="product_categories", back_populates="categories"
    )


class ProductCategory(Base):
    __tablename__ = "product_categories"
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
    PrimaryKeyConstraint("product_id", "category_id")

    def __repr__(self) -> str:
        return f"ProductCategory(product_id={self.product_id}, category_id={self.category_id})"


# class Quantity(Base):
#     __tablename__ = "quantities"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     unit = Column(String(50), nullable=False)
#     value = Column(Integer, nullable=False)

#     def __repr__(self) -> str:
#         return f"Quantity(unit={self.unit}, value={self.value})"


# class Price(Base):
#     pass


# class ProductPrice(Base):
#     pass
