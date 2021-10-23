import os
import urllib.parse as urlparse
import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

conn = redis.from_url("redis: //redis-12025.c291.ap-southeast-2-1.ec2.cloud.redislabs.com:12025")

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
