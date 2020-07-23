import sqlite3
from datetime import datetime

DB_PATH = 'test.db'

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

try:
    # execute方法的另外一种写法 在sql字符串中用？代替要插入的值， 以元组的方式 把要插入的数据作为 execute方法的第二个参数
    # c.execute("insert into user(username, password) values (?,?)", ('superman', '123456'))
    c.execute("update user set created = ? where id = ?", (datetime(2020, 7, 23, 8, 8, 8), 1))
    conn.commit()
except Exception as e:
    print(e)

num = conn.total_changes
print(num)
conn.close()
