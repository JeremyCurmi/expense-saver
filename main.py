from fastapi import FastAPI
from sqlalchemy.orm import Session

from app import models
from app.core import config, db
from app.routers import products
from app.services.services import ProductCrud

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()
app.include_router(products.router)
