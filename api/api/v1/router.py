from fastapi import APIRouter
from api.api.v1 import currywurst

router = APIRouter(prefix="/v1")

router.include_router(currywurst.router)