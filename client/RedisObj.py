# coding:utf-8
import redis


class RedisObj:
    def __init__(self, *args, **kwargs):
        self.__redis_host = kwargs.get('REDIS_HOST')
        self.__redis_port = kwargs.get('REDIS_PORT')
        self.__redis_db = kwargs.get('REDIS_DB')
        self.__redis_auth = kwargs.get('REDIS_PASSWD')

    def get_redis_pool(self):
        redis_handler = redis.ConnectionPool(host=self.__redis_host,
                           port=self.__redis_port, db=self.__redis_db, password=self.__redis_auth)

        return redis_handler

    def get_task(self, key):
        redis_con = redis.Redis(connection_pool=self.get_redis_pool())
        task_info = redis_con.rpop(key)
        return task_info

    def push_task(self, key, data, reverse=True):
        redis_con = redis.Redis(connection_pool=self.get_redis_pool())
        if reverse:
            redis_con.lpush(key, data)
        else:
            redis_con.rpush(key, data)

    def delete_task(self, key, data):
        redis_con = redis.Redis(connection_pool=self.get_redis_pool())
        redis_con.lrem(key, data, 1)

    def get_task_count(self, key):
        redis_con = redis.Redis(connection_pool=self.get_redis_pool())
        return redis_con.llen(key)

    def add_set(self, key, data):
        redis_con = redis.Redis(connection_pool=self.get_redis_pool())
        return redis_con.sadd(key, data)

    def rem_set(self, key, data):
        redis_con = redis.Redis(connection_pool=self.get_redis_pool())
        return redis_con.srem(key, data)

    def del_key(self, key):
        redis_con = redis.Redis(connection_pool=self.get_redis_pool())
        redis_con.delete(key)

    def random_member(self, key):
        redis_con = redis.Redis(connection_pool=self.get_redis_pool())
        task_info = redis_con.srandmember(key)
        return task_info
