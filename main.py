from fastapi import FastAPI

from app import models, db
from app.api.v1.api import api_router
from app.core import settings
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_URL)

@app.get("/")
def index():
    return {"message": "HomePage"}