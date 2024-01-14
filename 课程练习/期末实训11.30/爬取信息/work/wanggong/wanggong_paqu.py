import json
with open('wanggong.json', 'r', encoding='utf-8') as file:
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
        companyname=i['fullCompanyName'],
        companyloge=i['companyLogo'],
        jobdetails = i['jobHref'],
        companydetails = i['companyHref']
    )
print(_data)