import os

from app.utils import utils
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "Expense Saver"
    API_URL: str = "/api/v1"

    # owner info
    OWNER_ACCOUNT_NAME: str = "Jeris"
    OWNER_EMAIL: str = "jeris@gmail.com"
    OWNER_PHONE_NUMBER: int = 123
    OWNER_PASSWORD: str = "test"



    DATABASE_URL: str = utils.get_str_env("DATABASE_URL")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = utils.get_int_env("ACCESS_TOKEN_EXPIRE_MINUTES")
    SECRET_KEY: str = utils.get_str_env("SECRET_KEY")