from fastapi import APIRouter
from app.api.v1.routers import auth, user, category, products

api_router = APIRouter()
# TODO: add remaining routers
# api_router.include_router(roles.router)
# api_router.include_router(user_roles.router)
# api_router.include_router(accounts.router)
api_router.include_router(products.router)
api_router.include_router(category.router)
api_router.include_router(user.router)
api_router.include_router(auth.router)