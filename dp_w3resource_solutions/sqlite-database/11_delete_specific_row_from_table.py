"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 29/06/20
* @decription: Write a Python program to delete a specific row from a given SQLite table.
"""

import sqlite3


def display_table_rows():
    cur.execute('select * from ingredients')

    all_rows = cur.fetchall()
    for each in all_rows:
        print(each)


connection = sqlite3.connect('testing.sqlite')
cur = connection.cursor()

display_table_rows()

print('deleting...')

update_data_query = 'delete from ingredients where id = 20'
cur.execute(update_data_query)

display_table_rows()
connection.commit()
cur.close()
