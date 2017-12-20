# from . import views
from django.conf import settings
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import WebSiteViewset, CategoryViewset, ArticleViewset, ChapterViewset, no_end_article
from book.views import article_list, article_chapter


app_name = 'book'

router = DefaultRouter()


#配置goods的url
if settings.DEBUG:
    router.register(r'', WebSiteViewset, base_name="websites")
    router.register(r'(?P<website_id>.+)/categorys', CategoryViewset, base_name="categorys")

router.register(r'(?P<website_id>.+)/categorys/(?P<category_id>.+)/articles', ArticleViewset, base_name="articles")
router.register(r'(?P<website_id>.+)/categorys/(?P<category_id>.+)/articles/(?P<article_id>.+)/chapters', ChapterViewset, base_name="chapters")

urlpatterns = [
    # 网站的路由
    url(r'^(?P<website_id>.+)/categorys/(?P<category_id>.+)/articles/no-end$', no_end_article, name='no_end_article'),

    url(r'^$', article_list, name="article_list"),
    url(r'^article/(?P<article_id>.+)', article_chapter, name="article_chapter"),
    # rest framework 的路由
    url(r'^websites', include(router.urls)),
]
