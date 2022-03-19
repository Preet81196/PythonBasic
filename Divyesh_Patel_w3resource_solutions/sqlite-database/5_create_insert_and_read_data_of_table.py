"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/06/20
* @decription: Write a Python program to create a table and insert some records in that table.
            Finally selects all rows from the table and display the records.
"""

import sqlite3

connection = sqlite3.connect('testing.sqlite')
cur = connection.cursor()

initial_query = "CREATE TABLE if not exists ingredients(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar (100)" \
                ", recipe_id integer)"

cur.execute(initial_query)

insert_data_query = '''
insert into ingredients(name, recipe_id) values('Apple', 1);
insert into ingredients(name, recipe_id) values('Curd', 2);
insert into ingredients(name, recipe_id) values('Strawberry', 1);
insert into ingredients(name, recipe_id) values('Almonds', 1);
insert into ingredients(name, recipe_id) values('Oats', 2);
'''

cur.executescript(insert_data_query)

get_all_query = 'select * from ingredients'

cur.execute(get_all_query)
ingredients = cur.fetchall()

for ingredient in ingredients:
    print(ingredient)

cur.close()
