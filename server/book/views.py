from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


from .models import WebSite, Category, Article, Chapter
from .serializers import WebSiteSerializer, CategorySerializer, ArticleSerializer, ChapterSerializer

# Create your views here.


class WebSiteViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    create:
        创建站点
    list:
        站点列表数据
    retrieve:
        站点详情
    """
    queryset = WebSite.objects.all()
    serializer_class = WebSiteSerializer


class CategoryViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    create:
        创建分类
    list:
        站点分类列表
    retrieve:
        站点分类详情
    """
    def create(self, request, *args, **kwargs):
        _data = request.data.copy()
        _data['site'] = self.kwargs.get('website_id')
        serializer = self.get_serializer(data=_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = Category.objects.filter(site=self.kwargs.get('website_id'))
        return queryset

    serializer_class = CategorySerializer


class ArticleViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    create:
        创建文章
    list:
        返回当前分类文章列表
    retrieve:
        文章详情
    """
    def create(self, request, *args, **kwargs):
        _data = request.data.copy()
        _data['site'] = self.kwargs.get('website_id')
        _data['category'] = self.kwargs.get('category_id')
        serializer = self.get_serializer(data=_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = Article.objects.filter(category=self.kwargs.get('category_id'))
        return queryset

    serializer_class = ArticleSerializer


class ChapterViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    create:
        创建章节
    list:
        返回当前分类文章章节列表
    retrieve:
        章节详情
    """
    def get_queryset(self):
        queryset = Chapter.objects.filter(article=self.kwargs.get('article_id'))
        return queryset
    serializer_class = ChapterSerializer