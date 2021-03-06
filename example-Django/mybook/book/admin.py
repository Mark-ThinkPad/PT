from django.contrib import admin
from book import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']
    list_editable = ['title', 'pub_date']


@admin.register(models.Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'book', 'gender', 'comment']
    list_filter = ['name', 'book']
