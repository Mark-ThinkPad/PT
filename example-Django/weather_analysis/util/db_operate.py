import os
import django
import csv

# 手动启动 Django
# 配置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_analysis.settings')
# 启动 Django
django.setup()
# 需要在 Django 启动之后导入 Region 模型, 否则会报错
from region.models import Region
from django.db.models import Q


# 生成区域 level
def generate_region_level():
    print(Region.objects.filter(parent_id=0).exclude(id=0).update(level='0'))
    print(Region.objects.filter(parent__level='0').update(level='1'))
    print(Region.objects.filter(parent__level='2').update(level='2'))
    print(Region.objects.filter(parent__level='3').update(level='3'))


# 生成直辖市
def generate_municipality():
    Region.objects.filter(name__in=['北京市', '上海市', '天津市', '重庆市'])\
        .update(is_municipality=True)
    print(Region.objects.filter(name__in=['北京市', '上海市', '天津市', '重庆市']).query)


# 生成省会城市
def generate_province_capital():
    Region.objects.filter(id__endswith='0100')\
        .exclude(parent__is_municipality=True)\
        .update()


def set_display_region():
    # Q对象: 用于处理查询条件之间的 AND OR NOT
    print(Region.objects.filter(Q(is_municipality=True) | Q(is_province_capital=True)).query)


def insert_latitude_from_csv():
    with open('中国省市经纬度.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        # 跳过表头
        # print(reader.__next__())
        for row in reader:
            if row[0] == 'province':
                continue
            if row[1] == '':
                r = Region.objects.filter(name=row[0]).first()
            elif row[1] != '':
                r = Region.objects.filter(name=row[1]).first()
            if r:
                r.longitude = float(row[2])
                r.latitude = float(row[3])
                r.save()
                print(f'{r.name} 修改成功')


if __name__ == '__main__':
    # generate_region_level()
    # generate_municipality()
    set_display_region()
