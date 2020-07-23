import sqlite3

DB_PATH = 'test.db'


# 查询方法的封装
def fetch_one(sql: str) -> dict:
    """
    :param sql: SQL查询语句字符串
    :return: 以字典的形式返回单个查询结果
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
        return None
    fields = [t[0] for t in c.description]
    li = []
    for t in result:
        dic = {k: v for k, v in zip(fields, t)}
        li.append(dic)
    return li


def insert(tab_name, **kwargs):
    """
    提供一个通用的数据库插入方法
    :param tab_name: 要插入数据的表名
    :param kwargs: 要插入的数据
    :return:
    """
    pass


def update(tab_name, id, **kwargs):
    param = ','.join(['%s = ?' % k for k in kwargs.keys()])
    sql = "update %s set %s where id = %s" % (tab_name, param, id)
    print(sql)
    return dml(sql, *kwargs.values())


if __name__ == '__main__':
    print(fetch_all('select * from test'))
    print(fetch_one('select * from test'))
