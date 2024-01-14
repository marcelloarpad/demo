import pymysql
db = pymysql.connect(host="localhost", user="root", password="123456", database="MyTest", port=3306)
cursor = db.cursor()
try:
    cursor.execute("select * from student order by birth;")
    res = cursor.fetchall()
    for row in res:
        num = row[0]
        name = row[1]
        sex = row[2]
        birth = row[3]
        native = row[4]
        dorm = row[5]
        major = row[6]
        print(f"学号：{num},姓名：{name},出生日期：{birth}，住址：{native},宿舍：{dorm}，专业：{major}")
except:
    print("查不到数据记录")
db.close()