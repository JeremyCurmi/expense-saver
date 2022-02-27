import os
from typing import Any, Tuple

from app.structs.schemas import Response


def get_str_env(key: str, default: str = "") -> str:
    return str(os.getenv(key, default))


def response_success(data: Any = None, status_code: int = 200) -> Response:
    return Response(data=data, status_code=status_code)


def response_error(message: str, status_code: int = 400) -> Response:
    return Response(data=message, status_code=status_code)
