from fastapi import FastAPI

from currywurst_service.api.v1.router import router
from currywurst_service.service.event_service import create_connection 

from currywurst_service.api.middleware import RequestContextMiddleware


app = FastAPI()
app.include_router(router)
app.add_middleware(RequestContextMiddleware)

@app.on_event("startup")             
async def app_startup():
    app.state.rabbitmq_connection = await create_connection()

@app.on_event("shutdown")             
async def app_shutdown():
    await app.state.rabbitmq_connection.close()