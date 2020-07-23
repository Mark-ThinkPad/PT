import sqlite3
from datetime import datetime

DB_PATH = 'test.db'

def dml(sql_str, *args):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    print(sql_str)
    try:
        #  使用execute方法的 2个参数的形式来执行
        c.execute(sql_str, args)
        conn.commit()
    except Exception as e:
        print(e)
        return -1
    num = conn.total_changes
    conn.close()
    return num


def insert(tab_name, **kwargs):
    """
    在dml方法的基础上， 封装一个更加通用的 数据库 插入方法
    :param tab_name:  要插入数据的 表名
    :param kwargs:  要插入的数据
    :return:
    """
    fields_str = ','.join(kwargs.keys())
    values_str = ','.join('?' for i in range(len(kwargs)))
    sql_str = "insert into %s (%s) values (%s)" % (tab_name, fields_str, values_str)
    print(sql_str)
    return dml(sql_str, *kwargs.values())


def update(tab_name, id, **kwargs):
    """
    在dml方法的基础上， 封装一个更加通用的 数据库 更新方法
    :param tab_name: 要更新的表名
    :param id: 更新数据的id
    :param kwargs: 键值对的方式提供更新的字段与数值
    :return:
    """
    param_str = ','.join(['%s = ?' % k for k in kwargs.keys()])  # username = ?, password = ?
    sql_str = "update %s set %s where id = %s" % (tab_name, param_str, id)
    print(sql_str)
    return dml(sql_str, *kwargs.values())


print(insert('user', username="superdog2", password="123456"))
print(insert('product', name="麻辣鸡翅", price=30, num=90, category="零食"))
print(update('user', id=1, username='admin2', password='666666'))




