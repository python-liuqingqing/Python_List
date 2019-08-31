import redis

redis = redis.Redis(host='localhost', port=6379, db=0)
for i in range(10):
    redis.sadd('name',i)
# redis
print(redis.smembers('name'))