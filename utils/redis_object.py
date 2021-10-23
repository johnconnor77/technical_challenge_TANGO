import redis
import json
import os
import urllib.parse as urlparse

# redis = None
HEROKU = True
TEST_REDIS_URL = 'redis://localhost'
HEROKU_REDIS_URL = "redis://:p6d6c8a0c7ca8b15cbbe57a480c9e749f412a23a75de2948a32f50d6b246e5f9b@ec2-184-73-83-60.compute-1.amazonaws.com:14380"


def redis_connection():
    if HEROKU:
        redis_db = redis.from_url(HEROKU_REDIS_URL)
    else:
        redis_db = redis.from_url(TEST_REDIS_URL)
    return redis_db


