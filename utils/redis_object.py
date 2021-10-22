import aioredis
import json
import os

# redis = None

TEST_REDIS_URL = 'redis://localhost'
HEROKU_REDIS_URL = os.getenv('REDISTOGO_URL')

urlparse.uses_netloc.append('redis')
url = urlparse.urlparse(redis_url)


async def redis_connection():
    redis_db = await aioredis.Redis(Host=url.hostname, port=url.port, db=0, password=url.password)
    return redis_db
