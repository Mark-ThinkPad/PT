from django.db import models


class Region(models.Model):
    id = models.IntegerField('区域编号', primary_key=True)
    name = models.CharField('区域名称', max_length=30, null=False, blank=False)
    # 自关联, null=True设置的是数据库中的表定义相应字段可以为空
    # verbose_name 是说明字段
    # related_name 用于指定一找多时使用的名称
    parent = models.ForeignKey('self', verbose_name='父级区域',
                               related_name='children',
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    # 为每个区域, 生成一个字段, level 用于表明当前这个 region 是几级的
    level = models.CharField('区域级别', max_length=2, null=True, blank=True)
    # 经纬度
    latitude = models.FloatField('纬度', null=True, blank=True)
    longitude = models.FloatField('经度', null=True, blank=True)
    # 标志位: 是否为直辖市
    is_municipality = models.BooleanField('是否为直辖市', default=False, null=True)
    # 标志位: 是否为省会城市
    is_province_capital = models.BooleanField('是否为省会', default=False, null=True)
    # 标志位: 是否为省直辖城市
    is_province_municipality = models.BooleanField('是否为省直辖', default=False, null=True)
    # 标志位: 决定是否在地图上显示
    is_display = models.BooleanField('是否在地图上显示', default=False)

    def __str__(self):
        return self.name

    # 获取区域的省的名称
    def get_province_name(self):
        if self.level == '0':
            return self.name
        elif self.level == '1':
            return self.parent.name
        elif self.level == '2':
            return self.parent.parent.name
        else:
            return self.name

    class Meta:
        verbose_name = '区域信息'
        verbose_name_plural = verbose_name
