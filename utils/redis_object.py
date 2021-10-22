import aioredis
import json
from os import getenv

# redis = None

TEST_REDIS_URL = 'redis://localhost'


async def redis_connection():
    redis_db = await aioredis.Redis.from_url(TEST_REDIS_URL)
    return redis_db
