import requests
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"
}
base_ur1 = "http://www.baidu.com"
result1 = requests.request("GET",base_ur1)
with open("baidu.html","wb") as f:
    f.write(result1.content)


