import sqlite3

conn = sqlite3.connect("./test.db")
cur = conn.cursor()
cur.execute("SELECT * FROM scores")
# for i in data:
#     print(i)
print(cur.fetchall())
print(type(cur.fetchall()))
