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
from client.wenxue.proxy_article import get_update_page

red_conf = {
    'REDIS_HOST': settings.REDIS_HOST,
    'REDIS_PORT': settings.REDIS_PORT,
    'REDIS_DB': settings.REDIS_DB_ARTICLE,
    'REDIS_PASSWD': settings.REDIS_PASSWD,
}

red = RedisObj(**red_conf)
redis_push_key = "%s:%s:%s"
article_key = redis_push_key % (settings.REDIS_KEY_ARTICLE, 1, 2)
article_list_key = redis_push_key % (settings.REDIS_KEY_ARTICLE_LIST, 1, 2)

def get_first():
    count = 0
    while count < 20:
        r = red.get_task(article_key)
        # r = {
        #     "id": 2499,
        #     "url": 'http://t66y.com/htm_data/20/1712/2821863.html',
        # }
        # r = json.dumps(r)
        # print(r)
        # print(type(r))
        if(r):
            try:
                r = json.loads(r)
            except TypeError as e:
                r = json.loads(r.decode("utf-8"))
            dic = get_first_page(r.get('url'))
            if not dic:
                continue
            for dic_data in dic.get("data_list"):
                dic_data['url'] = r.get('url')
                dic_data['page'] = 1
                # dic_data['content'] = 'content'
                # print("++++++")
                # print(dic_data)
                print("++++++")
                _url = settings.WENXUE_ARTICLE_CHAPTER_URL % str(r.get('id'))
                print(_url)
                req = requests.post( _url, data = dic_data)
                # r = requests.get( _url)
                print(req.status_code)
                if(str(req.status_code) != '201'):
                    with open('re.html', 'w') as f:
                        f.write(req.text)
                print("++++++")
            # for other_url in dic.get("other_url_list"):
            #     dic = {
            #         'id': r.get('id'),
            #         'url': other_url
            #     }
            #     res = red.push_task(article_list_key, json.dumps(dic))
            #     print("%s----%s" % (res, dic.get('url')))

            # print(dic.get('data_list').get(''))1
            count += 1
            time.sleep(random.randint(1, 5))
        else:
            return


def get_other():
    count = 0
    while count < 20:
        r = red.get_task(article_list_key)
        # r = {
        #     "id": 2587,
        #     "url": 'http://t66y.com/htm_data/20/1712/2842337.html',
        # }
        # r = json.dumps(r)
        # print(r)
        # print(type(r))
        if(r):
            try:
                r = json.loads(r)
            except TypeError as e:
                r = json.loads(r.decode("utf-8"))
            dic = get_other_page(r.get('url'))
            if not dic:
                continue
            # print(dic)
            # break
            for dic_data in dic:
                print("++++++")
                _url = settings.WENXUE_ARTICLE_CHAPTER_URL % str(r.get('id'))
                print(_url)
                req = requests.post( _url, data = dic_data)
                # r = requests.get( _url)
                print(req.status_code)
                if(str(req.status_code) != '201'):
                    with open('re.html', 'w') as f:
                        f.write(req.text)
                    print(req.text)
                    print("-----")
                    print(dic_data)
                    return
                print("++++++")

            # count += 1
            time.sleep(random.randint(1, 5))
        else:
            return

def get_all():
    count = 0
    while count < 20:
        r = red.get_task(article_key)
        if(r):
            try:
                r = json.loads(r)
            except TypeError as e:
                r = json.loads(r.decode("utf-8"))
            dic = get_update_page(r.get('url'), r.get('current', 1))
            if not dic:
                continue
            for dic_data in dic:
                print("++++++")
                _url = settings.WENXUE_ARTICLE_CHAPTER_URL % str(r.get('id'))
                print(_url)
                req = requests.post( _url, data = dic_data)
                print(req.status_code)
                print("++++++")

            # count += 1
            time.sleep(random.randint(1, 5))
        else:
            return

if __name__ == '__main__':
    get_all()
