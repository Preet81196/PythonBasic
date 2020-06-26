"""
* @author: Divyesh Patel
* @email: pateldivyesh009@gmail.com 
* @date: 21/06/20
* @decription: Write a Python program to create a SQLite database and connect with the database
        and print the version of the SQLite database.
"""

import sqlite3

conn = sqlite3.connect('testing.sqlite')
cur = conn.cursor()

print('version:', sqlite3.version)
cur.close()
