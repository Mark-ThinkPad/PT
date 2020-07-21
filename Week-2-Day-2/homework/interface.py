import os
from data import (get_product_list, edit_product,
                  get_user_list)
from prettytable import PrettyTable


class Interface:
    MENU = []

    @staticmethod
    def cls():
        #  起到清屏的作用
        os.system('cls')

    def __init__(self):
        self.title = "请问您需要什么服务"
        self.opt_tips = "请输入您要操作的编号，按q键返回上级："

    def print(self):
        self.cls()
        print(self.title)
        print('-' * 40)
        self.print_menu()
        print('-' * 40)

    # 打印菜单方法
    def print_menu(self):
        for num, item in enumerate(self.MENU, start=1):
            print(str(num) + '\t' + item)

    #  用于处理界面逻辑的相关方法
    def run(self):
        self.print()
        choice = input(self.opt_tips)
        while choice != 'q':
            self.handler_user_choice(choice)
            self.print()
            choice = input(self.opt_tips)

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
    MENU = ['查看商品', '增加商品', '删除商品', '更新商品']

    def handler_user_choice(self, choice):
        if choice == '1':
            AdminProductListInterface().run()
        elif choice == '2':
            UnfinishedInterface().run()
        elif choice == '3':
            UnfinishedInterface().run()
        elif choice == '4':
            AdminProductEditInterface().run()


# 3.2.2.1 查看商品（列表）界面
class AdminProductListInterface(Interface):
    def print_menu(self):
        product_list = get_product_list()
        tb = PrettyTable()
        tb.field_names = ['编号', '商品名', '价格', '类别', '数量']
        for p in product_list:
            tb.add_row([p["id"], p["name"], p["price"], p["category"], p["num"]])
        print(tb)


# 3.2.2.4 更新(修改)商品信息界面
class AdminProductEditInterface(AdminProductListInterface):
    def __init__(self):
        self.title = "请输入您要编辑的商品的编号: "
        self.opt_tips = "请输入您要更新的商品编号，按q键返回："

    def handler_user_choice(self, choice):
        pid = choice
        name = input('请输入商品名, 不修改直接按回车: ')
        price = input('请输入价格, 不修改直接按回车: ')
        category = input('请输入类别, 不修改直接按回车: ')
        num = input('请输入库存数量, 不修改直接按回车: ')
        res = edit_product(pid, name, price, category, num)

        if res is None:
            print('商品编号不存在, 未作任何修改')
        else:
            print('修改成功')


# 3.2.3 查看用户信息(列表)界面
class AdminUserListInterface(Interface):
    def __init__(self):
        self.title = '用户情况如下: '
        self.opt_tips = "请输入您要操作的编号，按q键返回上级："

    def print_menu(self):
        user_list = get_user_list()
        tb = PrettyTable()
        tb.field_names = ['编号', '用户名', '密码', '角色']
        for u in user_list:
            tb.add_row([u['id'], u['username'], u['password'], u['role']])
        print(tb)
