import datetime

user_list = [
    {
        'id': 1,
        'username': 'admin',
        'password': '123456',
        'role': 'admin'
    },
    {
        'id': 2,
        'username': 'jack',
        'password': '123456',
        'role': 'user'
    },
    {
        'id': 3,
        'username': 'pony',
        'password': '123456',
        'role': 'user'
    },
    {
        'id': 4,
        'username': 'robin',
        'password': '123456',
        'role': 'user'
    },
    {
        'id': 5,
        'username': 'rose',
        'password': '123456',
        'role': 'user'
    },
]

product_list = [
    {
        'id': 1,
        'name': '辣条',
        'price': '10',
        'category': '零食',
        'num': 100
    },
    {
        'id': 2,
        'name': 'iPhoneXXX',
        'price': 10000,
        'category': '手机',
        'num': 100
    },
    {
        'id': 3,
        'name': '大猪蹄子',
        'price': 100,
        'category': '熟食',
        'num': 100
    },
    {
        'id': 4,
        'name': '大猪子肘',
        'price': 100,
        'category': '熟食',
        'num': 100
    },
    {
        'id': 5,
        'name': '大鸭脖子',
        'price': 100,
        'category': '熟食',
        'num': 100
    },
    {
        'id': 6,
        'name': '泰国榴莲',
        'price': 100,
        'category': '水果',
        'num': 100
    },
]

order_list = [
    {
        'id': 1,
        'username': 'jack',
        'product': '大猪蹄子',
        'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        'id': 2,
        'username': 'pony',
        'product': 'iphonxx',
        'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        'id': 3,
        'username': 'robin',
        'product': '辣条',
        'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
]


def get_user_list():
    return user_list


def get_product_list():
    return product_list


def get_order_list():
    return order_list


def edit_product(pid, name, price, category, num):
    for item in product_list:
        if int(pid) == item['id']:
            item['name'] = name if name else item['name']
            item['price'] = price if price else item['price']
            item['category'] = category if category else item['category']
            item['num'] = num if num else item['num']
            return item
    return None


def delete_product(pid):
    for item in product_list:
        if int(pid) == item['id']:
            product_list.remove(item)
            return True
    return False


def add_product(pid, name, price, category, num):
    item = {'id': pid, 'name': name, 'price': price, 'category': category, 'num': num}
    product_list.append(item)
    return item


if __name__ == '__main__':
    add_product(5, '三国演义', 999, '书籍', 2)
    print(product_list)
