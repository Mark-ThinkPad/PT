# 02. 摆放家具
class HouseItem(object):
    def __init__(self, name: str, area: float):
        self.name = name
        self.area = area

    def __str__(self) -> str:
        return self.name


class House(object):
    def __init__(self, house_type: str, area: float):
        self.house_type = house_type
        self.area = self.free_area = area
        self.item_list = []
    
    def __str__(self) -> str:
        return f'房子的户型为{self.house_type}, ' + \
               f'总面积为{self.area}平米, ' + \
               f'剩余面积有{self.free_area}, ' + \
               f'家具有: {self.item_list}'

    def add_item(self, item: HouseItem):
        if item.area > self.free_area:
            print('不能添加这件家具')
        else:
            self.free_area -= item.area
            self.item_list.append(item.name)


if __name__ == "__main__":
    bed = HouseItem('席梦思', 4)
    chest = HouseItem('衣柜', 2)
    table = HouseItem('餐桌', 1.5)

    villa = House('大别野', 500)
    villa.add_item(bed)
    villa.add_item(chest)
    villa.add_item(table)
    print(villa)

    small = House('鸽子笼', 6)
    small.add_item(bed)
    small.add_item(chest)
    small.add_item(table)
    print(small)
