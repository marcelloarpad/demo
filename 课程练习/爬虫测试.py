import requests
response = requests.get("https://www.baidu.com/")
if response.ok:
    print(response.text)
else:
    print("失败")