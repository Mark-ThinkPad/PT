import sqlite3

DB_PATH = 'test.db'

#
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

"""
dml方法的使用
"""

print(dml("insert into user(username, password) values ('superwomen', '123456')"))
print(dml("insert into user(username, password)  values (?,?)", 'superchild', '123456'))



