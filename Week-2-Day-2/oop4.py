class Dog:
    count = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_count_display(cls):
        print(f'{cls.count}只狗诞生了')

    @staticmethod
    def introduce():
        print('狗狗是人类的好朋友')


if __name__ == '__main__':
    wangcai = Dog('旺财')
    wangcai.introduce()
    Dog.introduce()
