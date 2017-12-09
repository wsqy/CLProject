from rest_framework import serializers

from .models import WebSite, Category, Article, Chapter


class WebSiteSerializer(serializers.ModelSerializer):
    """
    站点序列化类
    """
    class Meta:
        model = WebSite
        fields = "__all__"
        read_only_fields = ('create_time', "weights")


class CategorySerializer(serializers.ModelSerializer):
    """
    分类序列化类
    """
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('create_time', "weights")


class ArticleSerializer(serializers.ModelSerializer):
    """
    文章序列化类
    """
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ("weights", )


class ChapterSerializer(serializers.ModelSerializer):
    """
    章节序列化类
    """
    class Meta:
        model = Chapter
        fields = "__all__"
        # exclude = ("article", )

    def validate(self, data):
        print(data)
        return data