import sqlite3

DB_PATH = 'test.db'


# 查询方法的封装
def fetch_one(sql_str: str) -> dict:
    """
    :param sql_str: SQL查询语句字符串
    :return: 以字典的形式返回单个查询结果
    """
    con = sqlite3.connect(DB_PATH)
    c = con.cursor()
    c.execute(sql_str)
    result = c.fetchone()
    if not result:
        return None
    fields = [t[0] for t in c.description]
    dic = {k: v for k, v in zip(fields, result)}
    return dic


def fetch_all(sql_str: str) -> list:
    """
    :param sql_str: SQL查询语句字符串
    :return: 以列表的形式返回所有查询结果
    """
    con = sqlite3.connect(DB_PATH)
    c = con.cursor()
    c.execute(sql_str)
    result = c.fetchall()
    if not result:
        return None
    fields = [t[0] for t in c.description]
    li = []
    for t in result:
        dic = {k: v for k, v in zip(fields, t)}
        li.append(dic)
    return li


if __name__ == '__main__':
    print(fetch_all('select * from test'))
    print(fetch_one('select * from test'))
