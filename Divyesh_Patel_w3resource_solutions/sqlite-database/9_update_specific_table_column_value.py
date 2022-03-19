"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 29/06/20
* @decription: Write a Python program to update a specific column value of a given table and select
            all rows before and after updating the said table.
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

print('updating...')

update_data_query = 'update ingredients set recipe_id = 555 where id=1'
cur.execute(update_data_query)

display_table_rows()
connection.commit()
cur.close()