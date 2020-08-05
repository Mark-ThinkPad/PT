from django.contrib import admin
from weather_data import models


@admin.register(models.WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ['region', 'time', 'day_weather', 'day_weather_code',
                    'day_wind_power', 'max_degree', 'min_degree', 'created']


@admin.register(models.WeatherResult)
class WeatherResultAdmin(admin.ModelAdmin):
    list_display = ['region', 'result', 'created']
