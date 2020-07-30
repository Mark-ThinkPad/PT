import util
import requests
from datetime import datetime, timedelta
from region.models import Region
from weather_data.models import WeatherData
from weather_analysis.settings import (TX_WEATHER_URL, TX_WEATHER_PARAMS,
                                       TX_WEATHER_HEADERS)


# 根据区域城市来获取7日天气数据
def get_weather_by_region(region: Region):
    """
    根据区域获取天气信息
    :param region: 传入一个区域 model 对象
    :return: 返回7日天气信息的字典
    """
    params = TX_WEATHER_PARAMS
    params['province'] = region.get_province_name()
    params['city'] = region.name
    res = requests.get(TX_WEATHER_URL, params, headers=TX_WEATHER_HEADERS)
    return res.json()['data']['forecast_24h']


def get_weather_by_display_regions():
    """
    爬取要在地图上展示的城市的7日天气数据
    :return:
    """
    region_list = Region.objects.filter(is_display=True)
    for r in region_list:
        data = get_weather_by_region(r)
        # 把天气数据保存到数据库中
        if data:
            for v in data.values():
                WeatherData.objects.create(region=r, **v)
                print(f'{r.name} 天气已经成功保存')


def delete_weather_by_region(region: Region):
    """
    根据区域信息，删掉从当前时间开始 前一天到后6天的天气数据
    :param region: 传入一个区域 model 对象
    :return:
    """
    start = datetime.now() - timedelta(days=1)
    end = datetime.now() + timedelta(days=6)
    data = WeatherData.objects.filter(time__gte=start, time__lte=end, region=region)
    if data.count() > 0:
        print(data.delete())


def delete_weather_all():
    start = datetime.now() - timedelta(days=1)
    end = datetime.now() + timedelta(days=6)
    data = WeatherData.objects.filter(time__gte=start, time__lte=end)
    if data.count() > 0:
        print(data.delete())


if __name__ == '__main__':
    # sy = Region.objects.get(name='十堰市')
    # get_weather_by_region(sy)
    get_weather_by_display_regions()
    # delete_weather_by_region(sy)
    # delete_weather_all()
