from app.api.main import api_router
from fastapi import FastAPI

app = FastAPI(
    title="fastapi-playground",
    openapi_url="v0/openapi.json",
)


app.include_router(api_router, prefix="v0")
