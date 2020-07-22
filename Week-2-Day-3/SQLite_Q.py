import sqlite3

con = sqlite3.connect('test.db')
c = con.cursor()

c.execute('''
select * from test
''')

print(c.fetchall())

print(c.description)

con.close()
