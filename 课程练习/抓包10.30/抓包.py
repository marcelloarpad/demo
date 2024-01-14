import requests
base_url="http://www.baidu.com"
result=requests.request("GET",base_url)
print(result.text)
