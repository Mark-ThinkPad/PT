from prettytable import PrettyTable
from sql_methods import fetch_all


class ProductMixin:
    def print_menu(self):
        product_list = fetch_all('select * from product')
        tb = PrettyTable()
        tb.field_names = ['编号', '商品名', '价格', '类别', '数量']
        for p in product_list:
            tb.add_row([p["id"], p["name"], p["price"], p["category"], p["num"]])
        print(tb)

    def print_line(self):
        pass


class UserMixin:
    def print_menu(self):
        user_list = fetch_all('select * from user')
        tb = PrettyTable()
        tb.field_names = ['编号', '用户名', '密码', '角色']
        for u in user_list:
            tb.add_row([u['id'], u['username'], u['password'], u['role']])
        print(tb)

    def print_line(self):
        pass


class GuideMixin:
    def print_line(self):
        pass

    def get_opt_tips(self):
        return '按回车继续, 按q键返回上一级: '

    def get_info(self) -> tuple:
        username = input('请输入用户名: ')
        password = input('请输入密码: ')
        return username, password
