import redis
import json
import os
import urllib.parse as urlparse

# redis = None
HEROKU = True
TEST_REDIS_URL = 'redis://localhost'
HEROKU_REDIS_URL = "redis-12007.c100.us-east-1-4.ec2.cloud.redislabs.com:12007"

def redis_connection():
    if HEROKU:
        redis_db = redis.from_url(HEROKU_REDIS_URL)
    else:
        redis_db = redis.from_url(TEST_REDIS_URL)
    return redis_db


