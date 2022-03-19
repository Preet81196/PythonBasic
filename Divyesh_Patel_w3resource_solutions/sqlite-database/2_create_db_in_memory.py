"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/06/20
* @decription: Write a Python program to create a SQLite database connection to a database that resides in the memory.
"""

import sqlite3

connection = sqlite3.connect(':memory:')
cur = connection.cursor()

initial_query = "CREATE TABLE users(id int, firstname varchar(32), lastname varchar(32), dept int)"

cur.execute(initial_query)

get_all_tables = 'select * from SQLite_master where type="table"'

cur.execute(get_all_tables)
tables = cur.fetchall()

for table in tables:
    print(table)

cur.close()
