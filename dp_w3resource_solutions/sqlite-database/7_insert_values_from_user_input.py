"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/06/20
* @decription: Write a Python program to insert values to a table from user input.
"""

import sqlite3

connection = sqlite3.connect('testing.sqlite')
cur = connection.cursor()

initial_query = "CREATE TABLE if not exists ingredients(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar (100)" \
                ", recipe_id integer)"
cur.execute(initial_query)

ingredient = input('Enter ingredient name:')
recipe_id = int(input('Enter recipe id:'))

insert_data_query = 'insert into ingredients(name, recipe_id) values(?, ?);'
cur.execute(insert_data_query, (ingredient, recipe_id))

print('inserted at:', cur.lastrowid)

connection.commit()
cur.close()
