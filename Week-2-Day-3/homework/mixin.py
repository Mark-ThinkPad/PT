from prettytable import PrettyTable
from data import get_product_list


class ProductMixin:
    def print_menu(self):
        product_list = get_product_list()
        tb = PrettyTable()
        tb.field_names = ['编号', '商品名', '价格', '类别', '数量']
        for p in product_list:
            tb.add_row([p["id"], p["name"], p["price"], p["category"], p["num"]])
        print(tb)

    def print_line(self):
        pass