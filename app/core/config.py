import os

from app.utils import utils
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "Expense Saver"
    API_URL: str = "/api/v1"

    # owner info
    OWNER_ACCOUNT_NAME: str = utils.get_str_env("OWNER_ACCOUNT_NAME")
    OWNER_EMAIL: str = utils.get_str_env("OWNER_EMAIL")
    OWNER_PHONE_NUMBER: int = utils.get_str_env("OWNER_PHONE_NUMBER")
    OWNER_PASSWORD: str = utils.get_str_env("OWNER_PASSWORD")



    DATABASE_URL: str = utils.get_str_env("DATABASE_URL")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = utils.get_int_env("ACCESS_TOKEN_EXPIRE_MINUTES")
    SECRET_KEY: str = utils.get_str_env("SECRET_KEY")