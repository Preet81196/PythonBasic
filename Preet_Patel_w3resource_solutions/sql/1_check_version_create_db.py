import sqlite3

def create_connection(db_file):
    Conn = sqlite3.connect(db_file)
    cur =  Conn.cursor()

    print(sqlite3.version)
    cur.close()

create_connection("sqldata.db")

