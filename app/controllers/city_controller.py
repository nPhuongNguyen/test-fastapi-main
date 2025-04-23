from fastapi import HTTPException, status
from app.services.city_service import CityService
from app.schemas.city_schema import CitySchema

async def get_cities(service: CityService) -> list[CitySchema]:
    return await service.get_cities()  

async def get_city(city_id: int, service: CityService) -> CitySchema:
    city = await service.get_city_by_id(city_id)  
    if not city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"City with id {city_id} not found"
        )
    return city
