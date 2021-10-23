import redis
import json
import os
import urllib.parse as urlparse

# redis = None
HEROKU = True
TEST_REDIS_URL = 'redis://localhost'
#HEROKU_REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')


def redis_connection():
    if HEROKU:
        redis_url = os.getenv('REDISTOGO_URL')
        urlparse.uses_netloc.append('redis')
        url = urlparse.urlparse(redis_url)
        redis_db = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)
    else:
        redis_db = redis.from_url(TEST_REDIS_URL)
    return redis_db


