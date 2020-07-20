class MyClass:
    def __init__(self, name) -> None:
        self.name = name

    def __del__(self):
        print('销毁中')

    def __str__(self) -> str:
        return f'class name: {self.name}'

    # 方法的第一个参数是 self
    def func(self):
        print(self.name)


class SubClass(MyClass):
    # 方法重写
    def __str__(self) -> str:
        return f'sub class name: {self.name}'
    
    # 方法重写
    def func(self):
        print(f'sub class name: {self.name}')
    

if __name__ == "__main__":
    c = MyClass('haha')
    s = SubClass('sub class')
    print(s)
