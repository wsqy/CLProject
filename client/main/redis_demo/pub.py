import redis
pool = redis.ConnectionPool(host='123.206.210.196', port=6379, db=0, password='f886Yjhvuyfy76grhgdFYrtf')

r = redis.StrictRedis(connection_pool=pool)
while True:
    input_data = input("publish:")
    if input == 'over':
        print('停止发布')
        break;
    r.publish('spub', input)