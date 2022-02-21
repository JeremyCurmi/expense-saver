from app.models import Product
from app.services.product import get_product_by_id, get_product_by_name


def test_new_product(new_product):
    """When a new product is created, check schema"""
    assert new_product.id == 1
    assert new_product.name == "test_product"
    assert new_product.last_modified is not None


# TODO test get_product_by_id
def test_get_product_by_id(setup_db):
    product = get_product_by_id(setup_db, 1)
    assert product.id == 1
    assert product.name == "test_product_1"


def test_get_product_by_name(setup_db):
    """When a product is retrieved by id, check schema"""
    product = get_product_by_name(setup_db, "test_product_1")
    assert product.id == 1
    assert product.name == "test_product_1"


def test_get_products(setup_db):
    products = setup_db.query(Product).all()
    assert len(products) == 2
    assert products[1].name == "test_product_2"
