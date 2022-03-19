import sqlite3


connection = sqlite3.connect('sqldata.db')
cur = connection.cursor()

cur.execute('select * from students')

cur.execute('delete from students where id = 9')

connection.commit()
cur.close()
