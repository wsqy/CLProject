import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from book.models import Article
from utils.RedisObj import RedisObj

red_conf = {
    'REDIS_HOST': settings.REDIS_HOST,
    'REDIS_PORT': settings.REDIS_PORT,
    'REDIS_DB': settings.REDIS_DB_ARTICLE,
    'REDIS_PASSWD': settings.REDIS_PASSWD,
}

red = RedisObj(**red_conf)

redis_push_key = "%s:%s:%s"


@receiver(post_save, sender=Article)
def create_book(sender, instance=None, created=False, **kwargs):
    if created:
        dic = {
            "id": instance.id,
            "url": instance.url

        }
        red.push_task(redis_push_key % (settings.REDIS_KEY_ARTICLE, instance.site_id, instance.category_id), json.dumps(dic))
