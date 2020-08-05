import csv
import util
from django.db.models import Q
from region.models import Region


# 生成区域 level
def generate_region_level():
    print(Region.objects.filter(parent_id=0).exclude(id=0).update(level='0'))
    print(Region.objects.filter(parent__level='0').update(level='1'))
    print(Region.objects.filter(parent__level='1').update(level='2'))
    print(Region.objects.filter(parent__level='2').update(level='3'))


# 生成直辖市
def generate_municipality():
    Region.objects.filter(name__in=['北京市', '上海市', '天津市', '重庆市'])\
        .update(is_municipality=True)


# 生成省会城市
def generate_province_capital():
    Region.objects.filter(id__endswith='0100')\
        .exclude(parent__is_municipality=True)\
        .update(is_province_capital=True)


def set_display_region():
    # Q对象: 用于处理查询条件之间的 AND OR NOT
    Region.objects.filter(Q(is_municipality=True) | Q(is_province_capital=True))\
        .update(is_display=True)


# 从csv文件中导入 城市的经度和纬度信息
def insert_latitude_from_csv():
    with open('中国省市经纬度.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)

        for row in reader:
            # 跳过表头
            if row[0] == 'province':
                continue
            if row[1] == '':
                # 直接用get方法查的话 查不到的情况会报异常，所以用filter方法来做
                r = Region.objects.filter(name=row[0]).first()
            elif row[1] != '':
                r = Region.objects.filter(name=row[1]).first()
            if r:
                r.longitude = float(row[2])
                r.latitude = float(row[3])
                r.save()
                print(f'{r.name} 修改成功!')


# 初始化所有 region 的 short_name
def set_all_short_name():
    regions = Region.objects.all()
    for region in regions:
        region.set_short_name()


if __name__ == '__main__':
    # generate_region_level()
    # generate_municipality()
    # generate_province_capital()
    # set_display_region()
    # insert_latitude_from_csv()
    set_all_short_name()
