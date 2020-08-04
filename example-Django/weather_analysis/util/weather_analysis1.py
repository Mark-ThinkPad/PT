import util
from region.models import Region
from weather_data.models import WeatherData
from pandas import DataFrame
import pandas as pd


def get_region_weather_data(region: Region):
    return WeatherData.objects.filter(region=region)\
        .order_by('-created')[:6]\
        .values('day_weather', 'day_weather_code',
                'day_wind_power', 'max_degree', 'min_degree')


def get_region_weather_date(region: Region) -> list:
    return WeatherData.objects.filter(region=region)\
        .order_by('-created')[:6]\
        .values_list()


def get_region_weather_dataframe(region: Region) -> DataFrame:
    pass


if __name__ == '__main__':
    pass
