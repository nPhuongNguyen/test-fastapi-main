from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.logger import logger
import json
import redis.asyncio as redis  
from app.controllers.city_controller import get_cities, get_city
from app.schemas.city_schema import CitySchema
from app.dependencies import get_city_service
from app.redis_config import get_redis
router = APIRouter(tags=["Cities"])


@router.get("/redis/{key}")
async def check_redis_key(key: str, redis_list: redis.Redis = Depends(get_redis)):
    try:
        value = await redis_list.get(key)
        if value:
            logger.info(f"Lấy cache key: {key}")
            # Nếu là JSON thì trả về parse luôn
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return {"key": key, "value": value.decode("utf-8")}
        return {"message": f"Không tìm thấy key: {key}"}
    except redis.ConnectionError as e:
        logger.error(f"Redis error: {str(e)}")
        raise HTTPException(status_code=500, detail="Redis connection error")



@router.get("/cities/", response_model=List[CitySchema])
async def list_cities(redis_list: redis.Redis = Depends(get_redis), service=Depends(get_city_service)):
    cache_key = "cities:list"  # Key cho dữ liệu thành phố trong cache
    
    try:
        # Kiểm tra xem dữ liệu đã có trong cache chưa
        cached_data = await redis_list.get(cache_key)
        if cached_data:
            # Nếu có cache, trả về dữ liệu từ Redis
            logger.info("Dữ liệu lấy từ Redis")
            return [CitySchema(**city) for city in json.loads(cached_data)]
        
        # Nếu không có cache, lấy dữ liệu từ DB
        data = await get_cities(service)
        
        # Lưu dữ liệu vào Redis, với thời gian sống cache là 5 phút (300 giây)
        await redis_list.set(cache_key, json.dumps([city.dict() for city in data]), ex=300)
        logger.info("Dữ liệu lấy từ DB và lưu vào Redis")
        return data

    except redis.ConnectionError as e:
        # Xử lý lỗi Redis
        logger.error(f"Redis error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error with Redis")
    except Exception as e:
        # Xử lý lỗi chung
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred")

@router.get("/cities/{city_id}", response_model=CitySchema)
async def get_single_city(city_id: int, service=Depends(get_city_service)):
    try:
        return await get_city(city_id, service)
    except Exception as e:
        logger.error(f"Error getting city {city_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Error getting city information")