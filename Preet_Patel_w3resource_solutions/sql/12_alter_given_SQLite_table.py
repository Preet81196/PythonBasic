import sqlite3

connection = sqlite3.connect('sqldata.db')
cur = connection.cursor()

cur.execute ("""ALTER TABLE students rename COLUMN Enrollno TO PhoneNO;""")


cur.execute ('select * from students')

connection.commit()