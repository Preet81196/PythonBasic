"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/06/20
* @decription: Write a Python program to list the tables of given SQLite database file
"""

import sqlite3

connection = sqlite3.connect('testing.sqlite')
cur = connection.cursor()

get_all_tables = 'select * from SQLite_master where type="table"'

cur.execute(get_all_tables)

tables = cur.fetchall()

for table in tables:
    print(table)

cur.close()
