from typing import List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


from app.core.dependencies import get_db
from app.crud.crud_db import CategoryCrud
from app import schemas, models
from app.utils import response_error, response_success
from app.constants.role import Role
from app.core import dependencies as deps


router = APIRouter(
    prefix="/categories",
    tags=["category"],
)


@router.get("/", response_model=List[schemas.Category])
async def get_categories(db: Session = Depends(get_db),
                         current_user: models.User = Security(
                             deps.get_current_active_user,
                             scopes=Role.all_users,
                         ),
                         ):
    return CategoryCrud(db).get_all()


@router.get("/{id}", response_model=schemas.Response)
async def get_category_by_id(id: int, db: Session = Depends(get_db),
                             current_user: models.User = Security(
                                 deps.get_current_active_user,
                                 scopes=Role.all_users,
                             ),
                             ):
    category = CategoryCrud(db).get_by_id(id)
    if category:
        return response_success(category)
    else:
        return response_error(f"Category with id {id} not found")


@router.post("/", response_model=schemas.Response, status_code=201)
async def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db),
                          current_user: models.User = Security(
                              deps.get_current_active_user,
                              scopes=Role.registered_users,
                          ),
                          ):
    try:
        CategoryCrud(db).create(**category.dict())
    except IntegrityError as e:
        return response_error(f"Category already exists: {e}", status_code=400)
    return response_success(data="Category has been created", status_code=201)
