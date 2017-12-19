import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


from book.models import WebSite, Category, Article, Chapter
from book.serializers import WebSiteSerializer, CategorySerializer, ArticleSerializer, ChapterSerializer

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
    def create(self, request, *args, **kwargs):
        _data = request.data.copy()
        _data['article'] = self.kwargs.get('article_id')
        serializer = self.get_serializer(data=_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        old = Chapter.objects.filter(floor = serializer.validated_data['floor'], article = serializer.validated_data['article'])
        if old.count() == 0:
            serializer.save()
        else:
            for oo in old:
                if len(oo.content) < len(serializer.validated_data['content']):
                    oo.content = serializer.validated_data['content']
                    oo.save()


    def get_queryset(self):
        queryset = Chapter.objects.filter(article=self.kwargs.get('article_id'))
        return queryset
    serializer_class = ChapterSerializer


def no_end_article(request, website_id, category_id):
    article_list = Article.objects.filter(category=category_id, is_end=0, is_display=1).values('id', 'url', 'title', 'total_page', 'total_chapter')
    return HttpResponse(json.dumps(list(article_list)))