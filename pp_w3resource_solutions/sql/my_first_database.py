import _sqlite3


conn = _sqlite3.connect("table.db")
c = conn.cursor()


c.execute("select * from user")
data = c.fetchall()
for items in data:
    print(items)

conn.commit()
conn.close()