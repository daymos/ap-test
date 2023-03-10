from typing import Union
from fastapi import FastAPI

from currywurst_service.api.v1.router import router
from currywurst_service.service.event_service import create_connection 


app = FastAPI()
app.include_router(router)

@app.on_event("startup")             
async def app_startup():
    app.state.mb = await create_connection()
