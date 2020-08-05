from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from datetime import datetime, timedelta
from region.models import Region
from weather_data.models import WeatherData, WeatherResult
from weather_data.forms import RegionForm
from weather_analysis.settings import WEATHER_DATE_START, WEATHER_DATE_END
from util.weather_spider import delete_weather_by_region, get_weather_by_region
from util.weather_analyze import calculate_region_result


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
        delete_weather_by_region(region)
        new_data = get_weather_by_region(region)
        for v in new_data.values():
            WeatherData.objects.create(region=region, **v)
        data = WeatherData.objects.filter(region_id=region_id,
                                          time__range=(WEATHER_DATE_START, WEATHER_DATE_END))

    # 查询该地区是否计算出天气推荐指数
    if not region.weatherresult_set.filter(created__day=datetime.now().day):
        WeatherResult.objects.create(region=region, result=calculate_region_result(region))

    context = {
        'region': region,
        'data': data,
        'region_list': region_list,
        'region_weather': True
    }

    return render(request, 'weather_table.html', context)


def max_degree(request):
    region_list = Region.objects.filter(is_display=True)
    data = []
    # 生成最高温的数据列表
    for r in region_list:
        dic = {'name': r.name,
               'value': r.weatherdata_set.filter(time=datetime.now() + timedelta(days=1))
                   .first().max_degree}
        data.append(dic)

    geo_coord = {}
    for r in region_list:
        geo_coord[r.name] = [r.longitude, r.latitude]

    context = {
        'data': data,
        'geo_coord': geo_coord,
        'title': '全国主要城市明日高温情况',
        'num': 1.2,
        'color': 'orangered',
        'name': '高温℃',
        'max_degree': True
    }

    return render(request, 'map.html', context)


def min_degree(request):
    region_list = Region.objects.filter(is_display=True)
    data = []
    # 生成最低温的数据列表
    for r in region_list:
        dic = {'name': r.name,
               'value': r.weatherdata_set.filter(time=datetime.now() + timedelta(days=1))
                   .first().min_degree}
        data.append(dic)

    geo_coord = {}
    for r in region_list:
        geo_coord[r.name] = [r.longitude, r.latitude]

    context = {
        'data': data,
        'geo_coord': geo_coord,
        'title': '全国主要城市明日低温情况',
        'num': 1.2,
        'color': 'cyan',
        'name': '低温℃',
        'min_degree': True,
    }

    return render(request, 'map.html', context)


def wind_power(request):
    region_list = Region.objects.filter(is_display=True)
    data = []
    # 生成风力级数的数据列表
    for r in region_list:
        dic = {'name': r.name,
               'value': r.weatherdata_set.filter(time=datetime.now() + timedelta(days=1))
                   .first().day_wind_power}
        data.append(dic)

    geo_coord = {}
    for r in region_list:
        geo_coord[r.name] = [r.longitude, r.latitude]

    context = {
        'data': data,
        'geo_coord': geo_coord,
        'title': '全国主要城市明日风力情况',
        'num': 0.2,
        'color': 'yellow',
        'name': '风力级数',
        'wind_power': True
    }

    return render(request, 'map.html', context)


def recommend(request):
    region_list = Region.objects.filter(is_display=True)
    data = []
    for r in region_list:
        dic = {'name': r.name,
               'value': r.weatherresult_set.first().result}
        data.append(dic)

    geo_coord = {}
    for r in region_list:
        geo_coord[r.name] = [r.longitude, r.latitude]

    context = {
        'data': data,
        'geo_coord': geo_coord,
        'title': '全国主要城市旅游天气指数',
        'subtitle': '根据未来6天天气情况, 计算出是否适合旅游',
        'num': 3,
        'color': 'pink',
        'name': '推荐指数',
        'recommend': True
    }

    return render(request, 'map.html', context)
