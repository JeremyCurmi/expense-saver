import os
from datetime import datetime
from unicodedata import name

from app.core.dependencies import Base, SessionLocal
from app.models import (
    Category,
    CategoryType,
    Product,
    ProductCategory,
    ProductShop,
    Shop,
)
from app.models.models import Quantity
from app.crud.crud_db import (
    CategoryCrud,
    ProductCategoryCrud,
    ProductCrud,
    ProductShopsCrud,
    QuantityCrud,
    ShopCrud,
)
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@fixture
def set_env_vars():
    os.environ["APP_NAME"] = "test"
    yield
    del os.environ["APP_NAME"]


@fixture
def new_product():
    product = Product(
        id=1,
        name="test_product",
        updated_at=datetime.utcnow(),
    )
    return product


@fixture
def new_shop():
    shop = Shop(name="test_shop")
    shop.id = 1
    return shop


@fixture
def new_product_shop():
    product_shop = ProductShop(product_id=1, shop_id=1, price=1.0)
    return product_shop


@fixture
def new_category():
    return Category(name=CategoryType.food)


@fixture
def new_product_category():
    return ProductCategory(product_id=1, category_id=1)


@fixture(scope="session")
def setup_db():
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    seed_database(db)

    yield db

    db.close()
    Base.metadata.drop_all(bind=engine)


def seed_database(db):
    product = ProductCrud(db)
    product.create(name="test_product_1")
    product.create(name="test_product_2")

    shop = ShopCrud(db)
    shop.create(name="test_shop_1")
    shop.create(name="test_shop_2")

    quantity = QuantityCrud(db)

    product_shop = ProductShopsCrud(db)
    product_shop.create(product_id=1, shop_id=1, quantity_id=1, price=1.0)
    product_shop.create(product_id=1, shop_id=2, quantity_id=1, price=2.0)

    category = CategoryCrud(db)
    category.create(name=CategoryType.food)

    product_category = ProductCategoryCrud(db)
    product_category.create(product_id=1, category_id=1)
    product_category.create(product_id=2, category_id=1)
    product_category.create(product_id=2, category_id=3)
