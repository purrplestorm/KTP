# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from articles.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')

admin.site.register(Article, ArticleAdmin)
