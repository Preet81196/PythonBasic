"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/06/20
* @decription: Write a Python program to count the number of rows of a given SQLite table
"""

import sqlite3

connection = sqlite3.connect('testing.sqlite')
cur = connection.cursor()

insert_data_query = 'select count(*) from ingredients'
cur.execute(insert_data_query)

count = cur.fetchone()
print('rows:', count[0])

connection.commit()
cur.close()
