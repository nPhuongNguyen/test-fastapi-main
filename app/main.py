from fastapi import FastAPI
from app.routers import city_router
from app.controllers import healthcheck

app = FastAPI()

app.include_router(city_router.router, prefix="/api")

app.include_router(healthcheck.router)

