from bs4 import BeautifulSoup
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"
}
request = requests.get("https://yandex.com/video/search?family=yes&from=tabbar&text=%E6%97%A5%E6%9C%AC%E5%A5%B3%E4%BC%98", headers=headers)
html = request.text
print(html)
soup = BeautifulSoup(html,"html.parser")
all_video = soup.findAll("a", attrs={"class":"link serp-item__title i-bem link_js_inited", "data-bem":"{&quot;link&quot;:{}}", "tabindex":"0"})
for video in all_video:
    print(video)


