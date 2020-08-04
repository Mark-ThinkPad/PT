import util
from region.models import Region
from weather_data.models import WeatherData
from pandas import DataFrame
import pandas as pd


# 获取区域未来六天的天气数据 以列表+字典的形式返回数据
def get_region_weather_data(region: Region):
    return WeatherData.objects.filter(region=region)\
        .order_by('-created')[:6]\
        .values('day_weather', 'day_weather_code',
                'day_wind_power', 'max_degree', 'min_degree')


# 获取区域天气数据对应的日期，以列表形式返回数据
def get_region_weather_date(region: Region) -> list:
    return WeatherData.objects.filter(region=region)\
        .order_by('-created')[:6]\
        .values_list('time')


def get_region_weather_dataframe(region: Region) -> DataFrame:
    data = get_region_weather_data(region)
    date = get_region_weather_date(region)
    return pd.DataFrame(data, index=date)


if __name__ == '__main__':
    region = Region.objects.get(name='武汉市')
    print(get_region_weather_data(region))
    print(get_region_weather_date(region))
    df = get_region_weather_dataframe(region)
    print(df)
