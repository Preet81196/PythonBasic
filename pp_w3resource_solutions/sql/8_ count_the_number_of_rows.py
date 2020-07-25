""" 4.List the tables of given SQLite database file"""
import sqlite3

connection = sqlite3.connect('sqldata.db')
cur = connection.cursor()

cur.execute ("""INSERT INTO STUDENTS (name,subject) values('patel','DB');""")
cur.execute ("""INSERT INTO TEACHERS (name,subject) values('jaimin','maths');""")



cur.execute ('select * from students')

print(len(cur.fetchall()))
connection.commit()

