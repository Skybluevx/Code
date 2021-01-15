import sqlite3


# 创建于数据库的链接
coon = sqlite3.connect("./test.db")

# 创建一个游标 cursor
cur = coon.cursor()

# 建表的 sql 的语句
sql_text_1 = """CREATE TABLE scores
(姓名 TEXT,
班级 TEXT,
性别 TEXT,
语文 NUMBER,
数学 NUMBER,
英语 NUMBER);
"""

# 执行 sql语句
cur.execute(sql_text_1)

# 插入单挑数据
sql_text_2 = "INSERT INTO scores VALUES('A', '一班', '男', 96, 94, 98)"
cur.execute(sql_text_2)

# 插入多条数据
data = [("B", "一班", "女", 78, 87, 85),
        ("C", "一班", "男", 98, 84, 90)]

cur.executemany("INSERT INTO scores VALUES (?,?,?,?,?,?)", data)
# 连接完数据库并不会自动提交，所以需要手动 commit 你的改动 conn.commit()
coon.commit()
