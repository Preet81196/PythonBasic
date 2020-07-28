""" 4.List the tables of given SQLite database file"""
import sqlite3

connection = sqlite3.connect('sqldata.db')
cur = connection.cursor()

cur.execute ("""DROP TABLE IF EXISTS teachers;""")

cur.execute ( """CREATE TABLE teachers(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(100), subject varchar(100) )""" )
print("finish")

cur.execute ('select * from SQLite_master where type="table"')
tables = cur.fetchall()
connection.commit()

for data in tables:
    print(data)
connection.close()
