from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.city_model import City
import asyncio
class CityRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self)-> list[City]:
        try:
            result = await self.db.execute(select(City))
            await asyncio.sleep(1)
            return result.scalars().all()
        except Exception as e:
            raise Exception(f"Failed to fetch cities: {str(e)}")
    async def get_by_id(self, city_id: int):
        try:
            result = await self.db.execute(select(City).filter(City.city_id == city_id))
            return result.scalar_one_or_none()
        except Exception as e:
            print(f"Error in get_by_id: {e}")
            raise
