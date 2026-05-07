from django.contrib import admin
from .models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'view']
    readonly_fields = ('view',)
    list_filter = ['category']


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
