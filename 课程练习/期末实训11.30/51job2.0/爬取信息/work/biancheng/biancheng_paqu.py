import json
with open('biancheng.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 打印解析后的数据
data = data['resultbody']['job']['items']
_data = dict()
for i in data:
    _data[i['jobId']] = dict(
        name=i['jobName'],
        salary=i['provideSalaryString'],
        welfare=i['jobTags'],
        region=i['jobAreaString'],
        companyloge = i['companyLogo'],
        companyname = i['fullCompanyName']
    )
print(_data)