from typing import Union
from fastapi import FastAPI

from api.api.v1.router import router

app = FastAPI()

app.include_router(router)