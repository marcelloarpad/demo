import pymysql
import json
with open('源码.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 打印解析后的数据
data = data['resultbody']['job']['items']
_data = dict()
for i in data:
    _data[i['jobId']] = dict(
        name=i['jobName'],
        salary=i['provideSalaryString']
    )

jobdata = []
for a in _data.values():
    list_job = list(a.values())
    jobdata.append(list_job)
    print(list_job)
print(jobdata)

db = pymysql.connect(host="localhost", user="root", password="123456", database="51job", port=3306)
cursor = db.cursor()
for job in jobdata:
    sql = f"insert into 51job_table values('{job[0]}', '{job[1]}');"
    cursor.execute(sql)
    db.commit()
db.close()

