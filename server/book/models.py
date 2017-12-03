from django.db import models
import django.utils.timezone as timezone

from utils.validators import int_validators
# Create your models here.


# 网站信息表
class WebSite(models.Model):
    name = models.CharField(max_length=30, verbose_name="网站名")
    url = models.URLField(blank=True, verbose_name="官网", unique=True)
    create_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    weights = models.IntegerField(default=50, verbose_name="权重", validators=int_validators())

    class Meta:
        verbose_name = "站点"
        verbose_name_plural = verbose_name
        # 设置按权重排序，相同则按id倒序排列
        ordering = ['-weights', 'id']

    def __str__(self):
        return self.name


# 分类表
class Category(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name="分类")
    url = models.URLField(blank=True, verbose_name="主页地址", unique=True)
    create_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    weights = models.IntegerField(default=50, verbose_name="权重", validators=int_validators())
    sub_class = models.ForeignKey("self", verbose_name="父分类", null=True, blank=True)
    site = models.ForeignKey("WebSite", verbose_name="所属站点", null=False)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
        # 设置按权重排序，相同则按id倒序排列
        ordering = ['-weights', '-id']

    def __str__(self):
        return self.name


# 文章表
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="文章名")
    desc = models.TextField(blank=True, null=True,verbose_name="文章描述")
    url = models.URLField(blank=True, verbose_name="主页地址", unique=True)
    weights = models.IntegerField(default=50, verbose_name="权重", validators=int_validators())
    create_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    update_time = models.DateTimeField(verbose_name="更新时间", default=timezone.now)
    total_page = models.IntegerField(default=1, verbose_name="当前页数")
    is_end = models.BooleanField(default=False, verbose_name="是否完结")
    # name 作者名
    author = models.CharField(max_length=256, null=True, blank=True, verbose_name="作者信息")

    site = models.ForeignKey("WebSite", verbose_name="所属站点", null=False, default=None)
    category = models.ForeignKey("Category", verbose_name="所属分类", null=False)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        # 设置按权重排序，相同则按id倒序排列
        ordering = ['-weights', '-id']

    def __str__(self):
        return self.title


# 章节表
class Chapter(models.Model):
    article = models.ForeignKey("Article", verbose_name="所属文章", null=False)
    title = models.CharField(max_length=255, verbose_name="章节名", null=True, blank=True)
    content = models.TextField(blank=True, null=True,verbose_name="章节内容")
    url = models.URLField(blank=True, verbose_name="所在分页地址", unique=True)
    create_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    page = models.IntegerField(default=1, verbose_name="所在分页")
    floor = models.IntegerField(default=0, verbose_name="所在楼层")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title