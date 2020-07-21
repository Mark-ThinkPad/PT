import os
from prettytable import PrettyTable


class Interface:
    MENU = ['登录', '注册']

    @staticmethod
    def cls():
        os.system('cls')

    def __init__(self):
        self.title = '请问您需要什么服务'
        self.opt_tips = '请输入您要操作的编号, 按q键返回上级: '

    def print(self):
        self.cls()
        print(self.title)
        print('-' * 40)
        self.print_menu()
        print('-' * 40)

    def print_menu(self):
        for num, item in enumerate(self.MENU, start=1):
            print(str(num) + '\t' + item)

    def run(self):
        self.print()
        choice = input(self.opt_tips)
        while choice != 'q':
            self.handler_user_choice(choice)
            self.print()
            choice = input(self.opt_tips)

    def handler_user_choice(self, choice):
        pass


class UnfinishedInterface(Interface):
    def print_menu(self):
        print('功能正在开发中')


class AdminInterface(Interface):
    MENU = ['管理商品', '查看用户', '查看订单']

    def handler_user_choice(self, choice):
        if choice == '1':
            AdminProductInterface().run()
        elif choice == '2':
            UnfinishedInterface().run()


class AdminProductInterface(Interface):
    MENU = ['查看商品', '编辑商品', '删除商品', '更新商品']


class AdminProductListInterface(Interface):
    def print_menu(self):
        pass

