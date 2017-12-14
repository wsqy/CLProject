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

key = "article_other_url:1:2"
count = 0
for ar in Article.objects.filter(is_end=0):
    dic = {
        "id": ar.id,
        "url": ar.url,
        "title": ar.title,
    }
    print(ar.id)
    count += 1
    red.push_task(key, json.dumps(dic))

# key = "article_other_url:1:2"
#
# for ar in Article.objects.all():
#     dic = {
#         "id": ar.id,
#         "url": ar.url
#     }
#     print(ar.id)
#     red.push_task(key, json.dumps(dic))

# key = "article:1:2"
# ars = Article.objects.filter(is_end=0)
# for ar in ars:
#     c = Chapter.objects.filter(article=ar)
#     if c.count() == 0:
#         dic = {
#             "id": ar.id,
#             "url": ar.url
#         }
#         print(ar.id)
#         red.push_task(key, json.dumps(dic))

# # 太早的文章(10天前)而且章节只有一个的 就默认已完结
# import datetime
# ars = Article.objects.filter(is_end=0)
# for ar in ars:
#     c = Chapter.objects.filter(article=ar)
#     if c.count() == 1:
#         if (datetime.datetime.now() - c[0].create_time).days > 10:
#             ar.is_end = True
#             ar.save()

#
# # 只有一个章节的文章数
# ars = Article.objects.filter(is_end=0)
# counter = 0
# for ar in ars:
#     c = Chapter.objects.filter(article=ar)
#     if c.count() == 1:
#         counter += 1

# # 更新文章的时间为最后一个章节的时间
# ars = Article.objects.filter(is_end=1)
# counter = 0
# for ar in ars:
#     c = Chapter.objects.filter(article=ar)
#     if c.count() == 1:
#         ar.create_time, ar.update_time = ar.update_time, ar.create_time
#         ar.save()
#         counter += 1