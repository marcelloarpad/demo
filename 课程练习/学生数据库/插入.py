from pymysql import*
#创建查询数据库版本
db = connect(host="localhost", user="root", password="123456", database="MyTest", port=3306)
cursor1 = db.cursor()
sql1 = """insert into Student values 
('20295285','喜羊羊','男','2002/2/5','长沙','4-401','软件'),
('20255899','沸羊羊','男',null,'株洲','4-401','软件'),
('20245588','懒洋洋','女','2002/6/18','湘潭','2-203','软件'),
('20289985','美羊羊','女','2002/2/5','长沙','2-203','软件');"""
res = cursor1.execute(sql1)
print(f"插入{res}行数据成功！")
db.commit()
