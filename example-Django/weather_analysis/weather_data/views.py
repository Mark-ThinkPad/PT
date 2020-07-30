from django.shortcuts import render
from region.models import Region
from weather_data.models import WeatherData


def region_weather(request, region_id):
    region = Region.objects.get(id=region_id)
    data = WeatherData.objects.filter(region_id=region_id)[:7]

    context = {'region': region, 'data': data}
    return render(request, 'weather_table.html', context)
