import pymysql
#创建查询数据库版本
db = pymysql.connect(host="localhost", user="root", password="123456", database="mydb", port=3306)
cursor1 = db.cursor()
cursor1.execute("SELECT VERSION()")
data = cursor1.fetchone()
print(f"mysql版本{data}")
#插入
