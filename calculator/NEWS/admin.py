from django.contrib import admin
from NEWS.models import news
# Register your models here.

class news_admin(admin.ModelAdmin):
    list_display=('news_title','news_description')


admin.site.register(news,news_admin)