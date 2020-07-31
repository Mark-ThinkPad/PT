from django.shortcuts import render, HttpResponseRedirect
from region.models import Region
from weather_data.models import WeatherData
from weather_data.forms import RegionForm


def region_weather(request, region_id):
    region = Region.objects.get(id=region_id)

    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            region.latitude = form.cleaned_data.get('latitude')
            region.longitude = form.cleaned_data.get('longitude')
            region.is_display = form.cleaned_data.get('is_display')
            region.save()

        return HttpResponseRedirect(request.path)

    data = WeatherData.objects.filter(region_id=region_id)[:8]
    context = {'region': region, 'data': data}
    return render(request, 'weather_table.html', context)
