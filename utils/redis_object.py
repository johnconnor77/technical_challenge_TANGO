import aioredis
import json
import os

# redis = None

TEST_REDIS_URL = 'redis://localhost'
HEROKU_REDIS_URL = os.getenv('REDISTOGO_URL')


async def redis_connection():
    redis_db = await aioredis.Redis.from_url(HEROKU_REDIS_URL)
    return redis_db
