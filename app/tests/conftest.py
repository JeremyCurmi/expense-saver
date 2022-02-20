import os
from datetime import datetime
from unicodedata import name

from app.core.db import Base, SessionLocal
from app.models import Product
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
    product = Product(name="test_product")
    product.id = 1
    product.last_modified = datetime.now()
    return product


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

    product1 = Product(name="test_product_1")
    product2 = Product(name="test_product_2")
    db.add_all([product1, product2])
    db.commit()

    yield db

    db.close()
    Base.metadata.drop_all(bind=engine)
