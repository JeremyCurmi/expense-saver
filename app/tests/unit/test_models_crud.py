from sqlite3 import IntegrityError

import pytest
from app.models import CategoryType, Product
from app.services.services import (
    CategoryCrud,
    ProductCategoryCrud,
    ProductCrud,
    ProductShopsCrud,
)
from sqlalchemy import text
from sqlalchemy.exc import StatementError


def test_product_creation(setup_db):
    """When a new product is created, check schema"""
    Product = ProductCrud(setup_db)
    product = Product.get_by_id(1)
    assert product.id == 1
    assert product.name == "test_product_1"
    assert product.updated_at is not None


def test_get_product_by_id(setup_db):
    Product = ProductCrud(setup_db)
    product = Product.get_by_id(1)
    assert product.id == 1
    assert product.name == "test_product_1"


def test_get_product_by_name(setup_db):
    """When a product is retrieved by id, check schema"""
    Product = ProductCrud(setup_db)
    product = Product.get_by_name("test_product_1")
    assert product.id == 1
    assert product.name == "test_product_1"


def test_get_all_products(setup_db):
    Product = ProductCrud(setup_db)
    products = Product.get_all()
    assert len(products) == 2
    assert products[1].name == "test_product_2"

    product = Product.get_all(1)
    assert len(product) == 1
    assert product[0].name == "test_product_1"


def test_get_product_shops(setup_db):
    result = setup_db.execute(text("SELECT * FROM product_shops")).all()
    assert result is not None


def test_get_product_shops_by_product_id(setup_db):
    ProductShop = ProductShopsCrud(setup_db)
    product_shops = ProductShop.get_by_product_id(1)
    assert len(product_shops) == 2
    assert product_shops[0].product_id == 1


def test_get_product_shops_by_shop_id(setup_db):
    ProductShop = ProductShopsCrud(setup_db)
    product_shops = ProductShop.get_by_shop_id(1)
    assert len(product_shops) == 1
    assert product_shops[0].shop_id == 1


def test_category_creation(setup_db):
    Category = CategoryCrud(setup_db)
    _ = Category.create(name=CategoryType.drink)
    category = Category.get_by_name(CategoryType.drink)
    assert category.name == CategoryType.drink
    assert category.name != CategoryType.food

    # test with non existing category
    try:
        category = Category.create(name="test_category")
    except StatementError as err:
        setup_db.rollback()
    assert pytest.raises(StatementError)


def test_category_get_by_id(setup_db):
    Category = CategoryCrud(setup_db)
    category = Category.get_by_id(1)
    assert category.name == CategoryType.food


def test_product_category_creation(setup_db):
    ProductCategory = ProductCategoryCrud(setup_db)

    # successfully create new row
    _ = ProductCategory.create(product_id=1, category_id=4)
    product_category = ProductCategory.get_by_category_id(4)
    assert len(product_category) == 1
    assert product_category[0].category_id == 4
    assert product_category[0].product_id == 1
