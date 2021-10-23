import os
import urllib.parse as urlparse
import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

conn = redis.from_url("redis://:p6d6c8a0c7ca8b15cbbe57a480c9e749f412a23a75de2948a32f50d6b246e5f9b@ec2-184-73-83-60.compute-1.amazonaws.com:14380")

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
