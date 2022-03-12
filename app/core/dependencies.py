from typing import Generator
from fastapi import Security, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import jwt
import logging
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app import models, schemas
from app.crud import UserCrud
from app.core import settings
from app.core.security import ALGORITHM
from app.constants import Role


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_URL}/auth/access-token",
    scopes={
        Role.GUEST["name"]: Role.GUEST["description"],
        Role.ACCOUNT_ADMIN["name"]: Role.ACCOUNT_ADMIN["description"],
        Role.ACCOUNT_MANAGER["name"]: Role.ACCOUNT_MANAGER["description"],
        Role.ADMIN["name"]: Role.ADMIN["description"],
        Role.SUPER_ADMIN["name"]: Role.SUPER_ADMIN["description"],
    }
)

def get_db() -> Generator:
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        db.close()


def parse_token(token: str, exception) -> schemas.TokenPayload:
    """
    decode json token
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("id") is None:
            raise exception
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        logger.error("Error Decoding Token", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return token_data


def get_current_user(security_scopes: SecurityScopes,
                     db: Session = Depends(get_db),
                     token: str = Depends(reusable_oauth2)) -> models.User:
    authenticate_value = "Bearer"
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'

    credentials_exception = HTTPException(status_code=401,
                                          detail="Could not validate credentials",
                                          headers={"WWW-Authenticate": authenticate_value})

    token_data = parse_token(token, credentials_exception)

    user = UserCrud(db).get_by_id(id=token_data.id)
    if not user:
        raise credentials_exception

    no_role = security_scopes.scopes and not token_data.role
    bad_role = security_scopes.scopes and token_data.role not in security_scopes.scopes
    if no_role or bad_role:
        raise HTTPException(
            status_code=401,
            detail="Not enough permissions",
            headers={"WWW-Authenticate": authenticate_value},
        )
    return user

def get_current_active_user(current_user: models.User = Security(get_current_user, scopes=[],)) -> models.User:
    if current_user.is_active:
        return current_user
    raise HTTPException(status_code=400, detail="Inactive User")


