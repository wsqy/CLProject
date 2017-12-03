import redis
pool = redis.ConnectionPool(host='123.206.210.196', port=6379, db=0, password='f886Yjhvuyfy76grhgdFYrtf')

r = redis.StrictRedis(connection_pool=pool)
p = r.pubsub('')
p.subscribe()
for item in p.listen():
    print(item)
    if item['type'] == 'message':
        data =item['data']
        r.set('s',32)
        print(data)
        if item['data']=='over':
            break;
p.unsubscribe('spub')
print('取消订阅')
