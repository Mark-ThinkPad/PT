import sqlite3

DB_PATH = 'good4sale.db'


# 查询方法的封装
# def fetch_one(sql: str) -> dict:
#     """
#     :param sql: SQL查询语句字符串
#     :return: 以字典的形式返回单个查询结果
#     """
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute(sql)
#     result = c.fetchone()
#     if not result:
#         return None
#     fields = [t[0] for t in c.description]
#     dic = {k: v for k, v in zip(fields, result)}
#     return dic


def fetch_all(sql: str):
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
    con.close()
    li = []
    for t in result:
        dic = {k: v for k, v in zip(fields, t)}
        li.append(dic)

    return li


def add_one(sql: str) -> bool:
    """
    :param sql: SQL插入语句字符串
    :return: 插入成功返回true
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


if __name__ == '__main__':
    print(fetch_all('select * from user'))
