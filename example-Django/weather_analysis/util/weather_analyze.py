import util
from region.models import Region
from weather_data.models import WeatherData, WeatherResult
from weather_analysis.settings import OPTIMUM_MAX_TEMP, OPTIMUM_MIN_TEMP, WEIGHTS_DICT
from util.normalization import sigmoid, weather_type_normalization, wind_power_normalization
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


# 将区域的天气数据整理成DataFrame的形式
def get_region_weather_dataframe(region: Region) -> DataFrame:
    data = get_region_weather_data(region)
    date = get_region_weather_date(region)
    return pd.DataFrame(data, index=date)


# 对区域的天气数据进行归一化处理
def normalize_region_weather(region) -> DataFrame:
    df = get_region_weather_dataframe(region)
    new_df = pd.DataFrame()
    new_df['max_degree'] = 1.5 - (df['max_degree'] - OPTIMUM_MAX_TEMP).abs().apply(sigmoid)
    new_df['min_degree'] = 1.5 - (df['min_degree'] - OPTIMUM_MIN_TEMP).abs().apply(sigmoid)
    new_df['day_wind_power'] = df['day_wind_power'].apply(wind_power_normalization)
    new_df['day_weather_code'] = df['day_weather_code'].apply(weather_type_normalization)
    return new_df


# 计算给定城市的推荐指数
def calculate_region_result(region):
    try:
        df = normalize_region_weather(region)
        weights = pd.Series(WEIGHTS_DICT)
        return (df @ weights).sum()
    except:
        return -1


# 将要显示的城市的推荐结果计算出来
def save_display_region_result():
    region_list = Region.objects.filter(is_display=True)
    for r in region_list:
        WeatherResult.objects.create(region=r, result=calculate_region_result(r))
        print(f'{r}的结果已保存')


if __name__ == '__main__':
    # region = Region.objects.get(name='武汉市')
    # print(get_region_weather_data(region))
    # print(get_region_weather_date(region))
    # df = get_region_weather_dataframe(region)
    # print(df)
    save_display_region_result()
