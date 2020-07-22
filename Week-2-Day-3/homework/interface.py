import os
from time import sleep
from mixin import ProductMixin, UserMixin
from sql_methods import add_one
from data import (edit_product, delete_product, add_product)


class Interface:
    MENU = []

    @staticmethod
    def cls():
        #  起到清屏的作用
        os.system('cls')

    def __init__(self):
        self.title = "请问您需要什么服务"
        self.opt_tips = "请输入您要操作的编号，按q键返回上级："

    def print_line(self):
        print('-' * 40)

    def get_title(self):
        return self.title

    def get_opt_tips(self):
        return self.opt_tips

    def print(self):
        self.cls()
        print(self.get_title())
        self.print_line()
        self.print_menu()
        self.print_line()

    # 打印菜单方法
    def print_menu(self):
        for num, item in enumerate(self.MENU, start=1):
            print(str(num) + '\t' + item)

    #  用于处理界面逻辑的相关方法
    def run(self):
        self.print()
        choice = input(self.get_opt_tips())
        while choice != 'q':
            self.handler_user_choice(choice)
            self.print()
            choice = input(self.get_opt_tips())

    # 用于处理用户的输入项的业务逻辑
    def handler_user_choice(self, choice):
        pass


#  未完成界面
class UnfinishedInterface(Interface):
    def print_menu(self):
        print('功能正在开发中')


# 3.2.1 管理员功能引导界面
class AdminInterface(Interface):
    MENU = ['管理商品', '查看用户', '查看订单']

    def handler_user_choice(self, choice):
        if choice == '1':
            AdminProductInterface().run()
        elif choice == '2':
            AdminUserListInterface().run()
        elif choice == '3':
            UnfinishedInterface().run()


# 3.2.2 管理商品界面
class AdminProductInterface(Interface):
    MENU = ['查看商品', '新增商品', '删除商品', '更新商品']

    def handler_user_choice(self, choice):
        if choice == '1':
            AdminProductListInterface().run()
        elif choice == '2':
            AdminProductAddInterface().run()
        elif choice == '3':
            AdminProductDeleteInterface().run()
        elif choice == '4':
            AdminProductUpdateInterface().run()


# 3.2.2.1 查看商品（列表）界面
class AdminProductListInterface(ProductMixin, Interface):
    def get_title(self):
        return '商品列表'

    def get_opt_tips(self):
        return '按q键返回上一级：'


# 3.2.2.2 增加商品界面
class AdminProductAddInterface(Interface):
    def get_title(self):
        return '新增商品'

    def get_opt_tips(self):
        return '按回车开始输入商品信息, 按q键返回: '

    def handler_user_choice(self, choice):
        if choice == '':
            name = input('请输入商品名: ')
            price = float(input('请输入价格: '))
            category = input('请输入类别: ')
            num = int(input('请输入库存数量: '))
            sql = f"""
            insert into product (name, price, category, num)
            values ('{name}', {price}, '{category}', {num})
            """
            res = add_one(sql)
            if res:
                print('商品添加成功, 即将跳转至商品列表')
                sleep(2)
                AdminProductListInterface().run()
            else:
                print('商品添加失败, 即将刷新页面')
                sleep(2)



# 3.2.2.3 删除商品界面
class AdminProductDeleteInterface(ProductMixin, Interface):
    def get_title(self):
        return "删除商品"

    def get_opt_tips(self):
        return "请输入删除商品的编号，删除多个商品编号用逗号隔开,按q返回上级:"

    def handler_user_choice(self, choice):
        # 用户输入：    1,2,3,4,5   1
        li = choice.split(',')
        for i in li:
            delete_product(int(i))


# 3.2.2.4 更新商品信息界面
class AdminProductUpdateInterface(ProductMixin, Interface):
    def get_title(self):
        return "更新商品界面"

    def get_opt_tips(self):
        return "请输入您要更新的商品编号，按q返回上一级："

    def handler_user_choice(self, choice):
        pid = int(choice)
        name = input("请输入新的商品名称, 不修改直接回车：")
        price = input("请输入新的商品价格, 不修改直接回车：")
        category = input("请输入新的商品类别, 不修改直接回车：")
        num = input("请输入新的商品库存, 不修改直接回车：")
        edit_product(pid=pid, name=name, price=price, category=category, num=num)


# 3.2.3 查看用户信息(列表)界面
class AdminUserListInterface(UserMixin, Interface):
    def get_title(self):
        return '用户列表'

    def get_opt_tips(self):
        return '按q键返回上级：'
