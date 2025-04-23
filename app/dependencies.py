from fastapi import Depends
from app.services.city_service import CityService
from app.config.database import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession

async def get_city_service(db: AsyncSession = Depends(get_async_db)) -> CityService:
    return CityService(db)
