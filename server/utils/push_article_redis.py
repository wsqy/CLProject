import json
from book.models import Article, Chapter
from utils.RedisObj import RedisObj

red_conf = {
    'REDIS_HOST':  '123.206.210.196',
    'REDIS_PORT': '6379',
    'REDIS_DB': 3,
    'REDIS_PASSWD': 'f886Yjhvuyfy76grhgdFYrtf',
}

red = RedisObj(**red_conf)

# key = "article_other_url:1:2"
#
# for ar in Article.objects.all():
#     dic = {
#         "id": ar.id,
#         "url": ar.url
#     }
#     print(ar.id)
#     red.push_task(key, json.dumps(dic))

key = "article:1:2"
ars = Article.objects.filter(is_end=0)
for ar in ars:
    c = Chapter.objects.filter(article=ar)
    if c.count() == 0:
        dic = {
            "id": ar.id,
            "url": ar.url
        }
        print(ar.id)
        red.push_task(key, json.dumps(dic))