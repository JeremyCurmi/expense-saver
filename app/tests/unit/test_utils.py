import os

from app.utils.utils import get_str_env


def test_valid_get_str_env(set_env_vars):
    var = get_str_env("APP_NAME")
    assert isinstance(var, str)
    assert get_str_env("APP_NAME") == "test"


def test_invalid_with_default_value_get_str_env():
    var = get_str_env("UNKOWN_VARIABLE", "default_value")
    assert isinstance(var, str)
    assert var == "default_value"


def test_invalid_get_str_env():
    var = get_str_env("UNKOWN_VARIABLE")
    assert isinstance(var, str)
    assert var == ""
