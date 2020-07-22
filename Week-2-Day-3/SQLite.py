import sqlite3

con = sqlite3.connect('test.db')
c = con.cursor()

c.execute('''
create table test(
    ID int primary key,
    name varchar(20),
    age int
)
''')

con.commit()
con.close()
