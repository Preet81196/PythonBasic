"""2.Create a SQLite database connection to a database that resides in the memory"""


import sqlite3


Conn = sqlite3.connect(":memory:")                  #syntax :- ATTACH [DATABASE] ':memory:' AS database_name;
cur =  Conn.cursor()

print(cur.fetchall())
cur.close()



