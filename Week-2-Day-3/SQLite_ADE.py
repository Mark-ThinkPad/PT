import sqlite3

con = sqlite3.connect('test.db')
c = con.cursor()

c.execute('''
insert into test (ID, name, age) values (1, 'test2', 22)
''')

con.commit()
con.close()
