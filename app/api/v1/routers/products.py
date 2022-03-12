from typing import List
from fastapi import APIRouter, Depends, Security
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import models, schemas
from app.core import dependencies as deps
from app.crud import ProductCrud
from app.utils import response_error, response_success
from app.constants.role import Role

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


@router.get("/",response_model=List[schemas.Product])
async def get_products(db: Session = Depends(deps.get_db),
                       current_user: models.User = Security(
                           deps.get_current_active_user,
                           scopes=Role.all_users,
                       ),
                       ):
    return ProductCrud(db).get_all()


@router.get("/{id}", response_model=schemas.Response)
async def get_product_by_id(id: str,
                            db: Session = Depends(deps.get_db),
                            current_user: models.User = Security(
                                deps.get_current_active_user,
                                scopes=Role.all_users,
                            ),
                            ):
    product = ProductCrud(db).get_by_id(id)
    if product:
        return response_success(product)
    else:
        return response_error(f"Product with id {id} not found")


@router.get("/name/{name}", response_model=schemas.Response)
async def get_product_by_name(name: str,
                              db: Session = Depends(deps.get_db),
                              current_user: models.User = Security(
                                  deps.get_current_active_user,
                                  scopes=Role.all_users,
                              ),
                              ):
    product = ProductCrud(db).get_by_name(name)
    if product:
        return response_success(product)
    else:
        return response_error(f"Product with name {name} not found")


@router.post("/", response_model=schemas.Response, status_code=201)
async def create_product(product: schemas.ProductCreate,
                         db: Session = Depends(deps.get_db),
                         current_user: models.User = Security(
                             deps.get_current_active_user,
                             scopes=Role.registered_users,
                         ),
                         ):
    try:
        ProductCrud(db).create(**product.dict())
    except IntegrityError as e:
        return response_error(f"Product already exists: {e}", status_code=400)
    return response_success(data="Product has been created", status_code=201)


@router.delete("/{id}", response_model=schemas.Response)
async def delete_product_by_id(id: int, db: Session = Depends(deps.get_db),
                               current_user: models.User = Security(
                                   deps.get_current_active_user,
                                   scopes=Role.registered_users,
                               ),
                               ):
    try:
        ProductCrud(db).delete_by_id(id)
    except IntegrityError as e:
        return response_error(f"Product does not exist: {e}", status_code=400)
    return response_success(data="Product has been deleted")


@router.put("/{id}", response_model=schemas.Response)
async def update_product_by_id(
    id: int, product: schemas.ProductCreate, db: Session = Depends(deps.get_db),
    current_user: models.User = Security(
                                  deps.get_current_active_user,
                                  scopes=Role.registered_users,
                              ),
):
    ProductCrud(db).update(id, product)
    return response_success(data="Product has been updated")
