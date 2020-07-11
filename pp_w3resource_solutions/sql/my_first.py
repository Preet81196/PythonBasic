import _sqlite3
conn = _sqlite3.connect("table.db")

c = conn.cursor()


c.execute("select * from user")

print(c.fetchall())


conn.commit()

conn.close()