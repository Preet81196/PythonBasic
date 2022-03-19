"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 25/06/20
* @decription: Write a Python program to insert a list of records into a given SQLite table
"""

import sqlite3

connection = sqlite3.connect('testing.sqlite')
cur = connection.cursor()

initial_query = "CREATE TABLE if not exists ingredients(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar (100)" \
                ", recipe_id integer)"

cur.execute(initial_query)

insert_data_query = '''
insert into ingredients(name, recipe_id) values('Corn', 1);
insert into ingredients(name, recipe_id) values('Flexseed', 2);
insert into ingredients(name, recipe_id) values('Fish', 2);
insert into ingredients(name, recipe_id) values('Eggs', 2);
insert into ingredients(name, recipe_id) values('Veggies', 1);
'''

cur.executescript(insert_data_query)

get_counts = 'select count(*) from ingredients'

cur.execute(get_counts)
counts = cur.fetchall()

print('no of rows:', counts[0][0])

cur.close()
