from fastapi import APIRouter
from currywurst_service.api.v1 import currywurst

router = APIRouter(prefix="/v1")

router.include_router(currywurst.router)