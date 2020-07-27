from django.contrib import admin
from region import models


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
