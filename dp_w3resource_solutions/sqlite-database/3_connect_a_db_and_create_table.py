"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/06/20
* @decription: Write a Python program to connect a database and create a SQLite table within the database.
"""

import sqlite3

connection = sqlite3.connect('testing.sqlite')
cur = connection.cursor()

create_table = "CREATE TABLE if not exists recipes(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(100), type int)"

cur.execute(create_table)

get_all_tables = 'select * from SQLite_master where type="table"'

cur.execute(get_all_tables)

tables = cur.fetchall()

for table in tables:
    print(table)

cur.close()
