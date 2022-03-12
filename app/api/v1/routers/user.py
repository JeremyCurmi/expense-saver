from fastapi import APIRouter, Depends, Security, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pydantic.types import UUID4
from app.crud import UserCrud
from app.utils import response_error, response_success
from app import models, schemas
from app.core import dependencies as deps
from app.constants.role import Role

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/", response_model=List[schemas.User])
async def get_users(db: Session = Depends(deps.get_db),
                    current_user: models.User = Security(deps.get_current_active_user,
                                                         scopes=[Role.ADMIN["name"],
                                                                 Role.SUPER_ADMIN["name"]])):
    return UserCrud(db).get_all()

@router.get("/me", response_model=schemas.User)
async def get_my_user(db: Session = Depends(deps.get_db),
                      current_user: models.User = Depends(deps.get_current_active_user)):
    """
    Get own user
    """
    # role = None
    # if current_user.user_role:
    #     role = current_user.user_role.role.name
    # TODO re check this once user role table is created
    # TODO TEST!
    current_user_data = jsonable_encoder(current_user)
    return UserCrud(db).get_by_id(current_user_data["id"])

@router.put("/me", response_model=schemas.User)
async def update_my_user(full_name: str = Body(None),
                         phone_number: str = Body(None),
                         email: str = Body(None),
                         db: Session = Depends(deps.get_db),
                         current_user: models.User = Depends(deps.get_current_active_user),
                         ):
    """
    Update own user
    """
    current_user_data = jsonable_encoder(current_user)
    user = schemas.UserUpdate(**current_user_data)
    # TODO TEST!
    return UserCrud(db).update(current_user_data["id"], user)




@router.get("/{user_id}", response_model=schemas.User)
async def get_user_by_id(user_id: UUID4,
                         db: Session = Depends(deps.get_db),
                         current_user: models.User = Security(
                             deps.get_current_active_user,
                             scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
                         ),
                         ):
    return UserCrud(db).get_by_id(user_id)

@router.get("/{name}", response_model=schemas.Response)
async def get_user_by_name(name: str, db: Session = Depends(deps.get_db)):
    return UserCrud(db).get_by_name(name)

@router.post("/", response_model=schemas.User, status_code=201)
async def create_user(user: schemas.UserCreate,
                      db: Session = Depends(deps.get_db),
                      current_user: models.User = Security(
                          deps.get_current_active_user,
                          scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
                      ),
                      ):
    try:
        return UserCrud(db).create(user)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="The user with provided email already exists in the system.")


@router.delete("/{user_id}", response_model=schemas.Response)
async def delete_user_by_id(user_id: str,
                            db: Session = Depends(deps.get_db),
                            current_user: models.User = Security(
                                deps.get_current_active_user,
                                scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
                            ),
                            ):
    try:
        UserCrud(db).delete_by_id(user_id)
    except IntegrityError as e:
        return response_error(f"User does not exist: {e}", status_code=400)
    return response_success(data="User has been deleted")


@router.put("/{user_id}", response_model=schemas.User)
async def update_user_by_id(
        user_id: UUID4,
        user: schemas.UserUpdate,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Security(
                          deps.get_current_active_user,
                          scopes=[Role.ADMIN["name"], Role.SUPER_ADMIN["name"]],
                      ),
):
    """
    Update user
    """
    user_ = UserCrud(db).get_by_id(user_id)
    if not user_:
        raise HTTPException(status_code=404, detail="The user with this id does not exist in the system.")
    UserCrud(db).update(user_id, user)
    return user_