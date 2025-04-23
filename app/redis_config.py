import redis.asyncio as redis
from app.config.config import settings

# Tạo Redis client khi cần thiết
def get_redis():
    return redis.from_url(settings.REDIS_HOST, db=0)
