import sqlite3

DB_PATH = 'good4sale.db'


# 查询方法的封装
def fetch_one(sql: str):
    """
    :param sql: SQL查询语句字符串
    :return: 以字典的形式返回单个查询结果, 没有结果时返回 None
    """
    con = sqlite3.connect(DB_PATH)
    c = con.cursor()
    c.execute(sql)
    result = c.fetchone()
    if not result:
        return None
    fields = [t[0] for t in c.description]
    dic = {k: v for k, v in zip(fields, result)}
    return dic


def fetch_all(sql: str) -> list:
    """
    :param sql: SQL查询语句字符串
    :return: 以列表的形式返回所有查询结果
    """
    con = sqlite3.connect(DB_PATH)
    c = con.cursor()
    c.execute(sql)
    result = c.fetchall()
    if not result:
        return []
    fields = [t[0] for t in c.description]
    con.close()
    li = []
    for t in result:
        dic = {k: v for k, v in zip(fields, t)}
        li.append(dic)

    return li


def insert(sql: str) -> bool:
    """
    :param sql: SQL插入/删除语句字符串
    :return: 插入/删除成功返回true
    """
    con = sqlite3.connect(DB_PATH)
    c = con.cursor()
    try:
        c.execute(sql)
        con.commit()
        con.close()
        return True
    except:
        return False


def delete(sql: str) -> bool:
    """
    :param sql: SQL删除语句字符串
    :return: 删除成功返回 True, 否则返回 False
    """
    con = sqlite3.connect(DB_PATH)
    c = con.cursor()
    c.execute(sql)
    con.commit()
    rows = con.total_changes
    con.close()
    return bool(rows)


# 更新的封装代码跟删除是一样的, 但是我想把更新的函数名单独出来
def update(sql: str) -> bool:
    """
    :param sql: SQL更新语句字符串
    :return: 更新成功返回 True, 否则返回 False
    """
    return delete(sql)


def update_product(pid: int) -> bool:
    item = fetch_one(f'select * from product where id = {pid}')
    if item is None:
        return False

    name = input("请输入新的商品名称, 不修改直接回车：")
    price = input("请输入新的商品价格, 不修改直接回车：")
    category = input("请输入新的商品类别, 不修改直接回车：")
    num = input("请输入新的商品库存, 不修改直接回车：")

    item['name'] = name if name else item['name']
    item['price'] = float(price) if price else item['price']
    item['category'] = category if category else item['category']
    item['num'] = int(num) if num else item['num']

    res = update(f'''
    update product set name = '{item['name']}', price = {item['price']},
    category = '{item['category']}', num = {item['num']} where id = {pid}
    ''')

    return res


if __name__ == '__main__':
    print(fetch_all('select * from user'))
    print(update("update product set name = 'test' where id = 12"))
