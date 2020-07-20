# 03. 王者荣耀
class Item(object):
    def __init__(self, name: str, attack: int, defence: int):
        self.name = name
        self.attack = attack
        self.defence = defence

    def __str__(self) -> str:
        return self.name


class Hero(object):
    def __init__(self, name: str, life: int, 
                 attack: int, defence: int):
        self.name = name
        self.life = life
        self.attack = attack
        self.defence = defence
        self.item_list = []

    def __str__(self) -> str:
        s = f'{self.name}: 剩余血量为{self.life}, 装备有: '
        s += ', '.join(str(i) for i in self.item_list)
        return s

    def attack_one(self, hero):
        if hero.life <= 0:
            print(f'{hero.name}已经挂了, 就不要再鞭尸了吧!')
            return

        loss = self.attack
        for i in self.item_list:
            loss += i.attack

        loss -= hero.defence
        for i in hero.item_list:
            loss -= i.defence

        if loss <= 0:
            hero.life -= 0
        elif loss >= hero.life:
            hero.life = 0
        else:
            hero.life -= loss

    def equip_item(self, item: Item):
        if len(self.item_list) >= 6:
            print('武器和防具已满6件, 无法添加')
        else:
            self.item_list.append(item)
            print(f'{item.name}添加成功')


if __name__ == "__main__":
    weapon1 = Item('武器1', 60, 0)
    weapon2 = Item('武器2', 80, 0)
    armor1 = Item('防具1', 0, 10)
    armor2 = Item('防具2', 0, 20)

    Cheng = Hero('程咬金', 200, 60, 20)
    Sun = Hero('孙尚香', 160, 40, 10)

    Cheng.equip_item(weapon1)
    Cheng.equip_item(armor1)
    Sun.equip_item(weapon2)
    Sun.equip_item(armor2)

    Cheng.attack_one(Sun)
    Sun.attack_one(Cheng)
    print(Cheng)
    print(Sun)

    Sun.attack_one(Cheng)
    Cheng.attack_one(Sun)
    print(Cheng)
    print(Sun)

    Cheng.attack_one(Sun)
    print(Cheng)
