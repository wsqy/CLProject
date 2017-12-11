import xadmin
from xadmin import views

from book.models import WebSite, Category, Article, Chapter

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕学生鲜后台"
    site_footer = "mxshop"
    # menu_style = "accordion"


class WebSiteAdmin(object):
    list_display = ('name', 'url', 'weights')


class CategoryAdmin(object):
    list_display = ('name', 'sub_class', 'site', '')


class ArticleAdmin(object):
    list_display = ('title', 'update_time', 'total_page', 'is_end')
    list_filter = ('title', 'is_end')
    search_fields = ('title', )
    list_editable=('is_end', )


class ChapterAdmin(object):
    list_display = ('title', 'article', 'create_time')
    list_filter = ('article',)
    search_fields = ('article', )


xadmin.site.register(WebSite, WebSiteAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Chapter, ChapterAdmin)


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)