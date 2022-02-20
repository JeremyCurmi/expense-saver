import os

from app.utils import utils
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    app_name: str = utils.get_str_env("APP_NAME")
    DATABASE_URL: str = utils.get_str_env("DATABASE_URL")


settings = Settings()
