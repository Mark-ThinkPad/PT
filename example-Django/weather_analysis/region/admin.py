from django.contrib import admin
from region import models


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'level', 'is_municipality', 'is_province_capital',
                    'is_display', 'name', 'short_name', 'parent']
    list_editable = ['is_display', 'short_name']
    search_fields = ['name', 'short_name']
    list_filter = ['parent']
