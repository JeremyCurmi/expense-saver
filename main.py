from sqlalchemy.orm import Session

from app import models
from app.core import config, db
from app.services.product import get_product_by_id, get_product_by_name, get_products

models.Base.metadata.create_all(bind=db.engine)

# Dependency
def get_db():
    db_ = db.SessionLocal()
    try:
        yield db_
    finally:
        db_.close()


if __name__ == "__main__":
    db_ = db.SessionLocal()
    prod = get_product_by_id(db_, 1)
    print(type(prod))
    print(prod)
