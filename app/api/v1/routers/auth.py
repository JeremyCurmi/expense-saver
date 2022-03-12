from fastapi import APIRouter, Body, Depends, HTTPException
from typing import Any
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app import schemas, core, models
from app.core import settings
from app.core import dependencies as deps
from app.crud import UserCrud

router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/access-token", response_model=schemas.Token)
def login_access_token(db: Session = Depends(deps.get_db),
                       form_data: OAuth2PasswordRequestForm = Depends(),
                       ):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = UserCrud(db).authenticate(email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="User is not active")

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    token_payload = {
        "id": str(user.id),
        "role": user.get_role(),
        "account_id": str(user.account_id),
    }

    return {
        "access_token": core.auth.create_access_token(token_payload, expires_delta=access_token_expires),
        "token_type": "bearer",
    }




@router.post("/test-token", response_model=schemas.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)):
    """
    test access token
    """
    return current_user

@router.post("/hash-password", response_model=str)
def hash_password(password: str = Body(..., embed=True)) -> Any:
    """
    hash password
    """
    return core.auth.get_password_hash(password)