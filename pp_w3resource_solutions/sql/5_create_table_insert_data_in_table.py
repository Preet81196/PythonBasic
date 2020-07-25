import sqlite3

connection = sqlite3.connect('sqldata.db')
cur = connection.cursor()

cur.execute ("""INSERT INTO STUDENTS VALUES('1','preet', 'python');""")

cur.execute ("""INSERT INTO STUDENTS VALUES('2','Divlo', 'java');""")

cur.execute ( """INSERT INTO TEACHERS VALUES('1','viral', 'python');""" )
cur.execute ( """INSERT INTO TEACHERS VALUES('2','Anand', 'java');""" )

cur.execute ('select * from students')

tables = cur.fetchall()
connection.commit()
for data in tables:
    print(data)
connection.close()
