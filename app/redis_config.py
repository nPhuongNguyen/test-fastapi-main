import redis.asyncio as redis

# Tạo Redis client khi cần thiết
def get_redis():
    return redis.from_url("redis://localhost:6379", db=0)
