import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect("./test.db")
cur = conn.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS test2(id INTEGER PRIMARY KEY ,name text, age integer)")
# data = (1, "aqq", 20)
# cur.execute(f"insert into test2 values {data}")
# cur.execute("insert into test2 values (?,?,?)", (5, "leno", 22))
cur.execute("select * from test2 where id=2")
for i in cur:
    print(i[0], i[1], i[2])

conn.commit()
cur.close()
conn.close()
