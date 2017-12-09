import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.path.dirname(BASE_DIR))
sys.path.insert(2, os.path.dirname(os.path.dirname(BASE_DIR)))
import json
import time
import random
import requests
from client import settings
from client.RedisObj import RedisObj
from client.wenxue.proxy_article import get_first_page

red_conf = {
    'REDIS_HOST': settings.REDIS_HOST,
    'REDIS_PORT': settings.REDIS_PORT,
    'REDIS_DB': settings.REDIS_DB_ARTICLE,
    'REDIS_PASSWD': settings.REDIS_PASSWD,
}

# red = RedisObj(**red_conf)
# redis_push_key = "%s:%s:%s"
# key = redis_push_key % (settings.REDIS_KEY_ARTICLE, 1, 2)
# r = red.get_task(key)
# print(r)
# print(json.loads(r))

def main():
    count = 0
    while count < 1:
        # r = red.get_task(key)
        r = {
            "id": 2546,
            "url": 'http://t66y.com/htm_data/20/1712/2829288.html',
        }
        r = json.dumps(r)
        if(r):
            # dic_data = {
            #     "page": 1,
            #     "title": "暑假上了大学宿舍的美女少妇楼管",
            #     "content": "skjj",
            #     "url": "http://t66y.com/htm_data/20/1712/2829288.html",
            #     "create_time": "2017-12-08 09:56",
            #     "floor": 0
            # }
            # r = requests.post( settings.WENXUE_ARTICLE_CHAPTER_URL % '2546', json = json.dumps(dic_data, ensure_ascii=False))
            # print("111111")
            # print(r.status_code)
            # print("111111")
            # print(r.text)
            # print("111111")
            # return
            r = json.loads(r)
            dic = get_first_page(r.get('url'))
            dic_data_list = dic.get("data_list")
            for dic_data in dic_data_list:
                dic_data['url'] = r.get('url')
                dic_data['page'] = 1
                # dic_data['content'] = 'content'
                print("++++++")
                print(json.dumps(dic_data, ensure_ascii=False))
                print("++++++222")
                _url = settings.WENXUE_ARTICLE_CHAPTER_URL % str(r.get('id'))
                print(_url)
                req = requests.post( _url, json = json.dumps(dic_data, ensure_ascii=False, allow_redirects=False))
                # r = requests.get( _url)
                print(req.status_code)
                print("++++++111")
                print(req.text)
                print("++++++")
                print(req.headers)
                print("++++++")
            # print(dic.get('data_list').get(''))1
            count += 1
            time.sleep(random.randint(1, 5))
        else:
            return

if __name__ == '__main__':
    main()
