from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from region.models import Region
from weather_data.models import WeatherData
from weather_data.forms import RegionForm
from util.weather_spider import delete_weather_by_region
from weather_analysis.settings import WEATHER_DATE_START, WEATHER_DATE_END


def region_weather(request, region_id):
    region = Region.objects.get(id=region_id)
    region_list = Region.objects.filter(level='0')

    if request.method == 'POST':
        form = RegionForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            region.latitude = form.cleaned_data.get('latitude')
            region.longitude = form.cleaned_data.get('longitude')
            region.is_display = form.cleaned_data.get('is_display')
            region.save()
            messages.success(request, '城市信息修改成功!', extra_tags='success')
        else:
            messages.error(request, '输入的数据有误, 修改失败!', extra_tags='danger')
        return HttpResponseRedirect(request.path)

    data = WeatherData.objects.filter(region_id=region_id,
                                      time__range=(WEATHER_DATE_START, WEATHER_DATE_END))
    if data.count() < 8:
        pass

    context = {'region': region, 'data': data, 'region_list': region_list}
    return render(request, 'weather_table.html', context)
