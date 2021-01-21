import pymysql


conn = pymysql.connect(host="localhost", user="root", password="", database="test", port=3306)

cursor = conn.cursor()
result = cursor.execute("select 1")
print(result)

conn.close()
