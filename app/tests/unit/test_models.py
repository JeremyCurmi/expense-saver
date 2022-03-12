import pytest
from app import models
from app.models import CategoryType, Product
from app.crud.crud_db import CategoryCrud, ProductCategoryCrud, ProductShopsCrud
from sqlalchemy.exc import IntegrityError


def assert_model_columns(model: models.Base, columns):
    table_columns = model.__table__.columns.keys()
    assert set(table_columns) == set(columns)


def test_new_product(new_product):
    """When a new product is created, check schema"""
    assert_model_columns(new_product, ["id", "name", "description", "updated_at"])
    assert new_product.id == 1
    assert new_product.name == "test_product"
    assert new_product.updated_at is not None


def test_shop_creation(new_shop):
    assert_model_columns(new_shop, ["id", "name"])
    assert new_shop.name == "test_shop"
    assert new_shop.id == 1


def test_category_creation(new_category):
    """When a new category is created, check schema"""
    assert_model_columns(new_category, ["id", "name"])
    assert new_category.name == CategoryType.food


def test_category_name_uniqeness(setup_db):
    """When a new category is created, check name uniqeness"""
    Category = CategoryCrud(setup_db)
    try:
        Category.create(name=CategoryType.food)
    except IntegrityError as err:
        setup_db.rollback()
    assert pytest.raises(IntegrityError)


def test_product_category_creation(new_product_category):
    """When a new product category is created, check schema"""
    assert_model_columns(new_product_category, ["product_id", "category_id"])
    assert new_product_category.product_id == 1
    assert new_product_category.category_id == 1


def test_product_shop_creation(new_product_shop):
    assert_model_columns(
        new_product_shop, ["product_id", "shop_id", "quantity_id", "price"]
    )
    assert new_product_shop.product_id == 1
    assert new_product_shop.shop_id == 1
    assert isinstance(new_product_shop.price, float)


def test_product_shop_foreign_key_constraint(setup_db):
    """When a new product shop is created, check foreign key constraint"""
    ProductShop = ProductShopsCrud(setup_db)
    try:
        ProductShop.create(product_id=1, shop_id=2)
    except IntegrityError as err:
        setup_db.rollback()
    assert pytest.raises(IntegrityError)


def test_product_shop_primary_key_constraint(setup_db):
    """When a new product shop is created, check primary key constraint"""
    ProductShop = ProductShopsCrud(setup_db)
    try:
        ProductShop.create(product_id=1, shop_id=1)
    except IntegrityError as err:
        setup_db.rollback()
    assert pytest.raises(IntegrityError)


def test_product_category_primary_key_constraint(setup_db):
    """When a new product shop is created, check primary key constraint"""
    ProductCategory = ProductCategoryCrud(setup_db)
    try:
        ProductCategory.create(product_id=1, category_id=1)
    except IntegrityError as err:
        setup_db.rollback()
    assert pytest.raises(IntegrityError)


# TODO: test quantities
