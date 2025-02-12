from app.api.v0 import items, login, private, users, utils
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(items.router)
