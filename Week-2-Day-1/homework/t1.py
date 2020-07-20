# 01. 李雷爱跑步
class Person(object):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
    
    def __str__(self) -> str:
        return f'{self.name}的体重为{self.weight}公斤'
    
    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


if __name__ == "__main__":
    LiLei = Person('李雷', 75.0)
    LiLei.eat()
    LiLei.run()
    LiLei.run()
    LiLei.run()
    print(LiLei)

    HanMeiMei = Person('韩梅梅', 45.0)
    HanMeiMei.eat()
    HanMeiMei.run()
    HanMeiMei.run()
    HanMeiMei.run()
    print(HanMeiMei)
