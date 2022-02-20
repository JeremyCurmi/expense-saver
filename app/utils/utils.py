import os


def get_str_env(key: str, default: str = "") -> str:
    return str(os.getenv(key, default))
