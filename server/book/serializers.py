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


    def validate(self, validated_data):
        print("validate")
        print(validated_data)
        print("validate")
        return validated_data

    def validate_name(self, name):
        print("validate_name")
        print(name)
        print("validate_name")
        return name

    def validate_site(self, site):
        print("validate_site")
        print(site)
        print("validate_site")
        return site

    def validate_url(self, url):
        print("validate_url")
        print(url)
        print("validate_url")
        return url


class ArticleSerializer(serializers.ModelSerializer):
    """
    文章序列化类
    """
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ('category', "weights")


class ChapterSerializer(serializers.ModelSerializer):
    """
    章节序列化类
    """
    class Meta:
        model = Chapter
        fields = "__all__"