from fastapi import FastAPI

from app import models
from app.core import db
from app.routers import category, products

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()
app.include_router(products.router)
app.include_router(category.router)
