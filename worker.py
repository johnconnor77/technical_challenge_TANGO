import os
import urllib.parse as urlparse
import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_url = "redis-12007.c100.us-east-1-4.ec2.cloud.redislabs.com:12007"
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
