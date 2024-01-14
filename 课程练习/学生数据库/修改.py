import pymysql
db = pymysql.connect(host="localhost", user="root", password="123456", database="mydb", port=3306)
cursor = db.cursor()

sid = '20225523'
sname = "李明"
sbirthday = "2010.2.5"

try:
    cursor.execute(f"undata t_studenstinfo set s_nane='{sname}',s_birthday='{sbirthday}'where s-id='{sid}'")