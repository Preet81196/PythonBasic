"""3.Write a Python program to connect a database and create a SQLite table within the database."""


import sqlite3

connection = sqlite3.connect('sqldata.db')
cur = connection.cursor()

cur.execute ( """
DROP TABLE IF EXISTS students;""")

cur.execute ( """CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(100), subject varchar(100) )""" )
print("finish")

cur.execute ('select * from SQLite_master where type="table"')
tables = cur.fetchall()

for data in tables:
    print(data)
connection.close()
