from bs4 import BeautifulSoup
import requests
heards = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"
}
requsta = requests.get("https://movie.douban.com/top250", headers = headers)
requst = requsta.text
soup = BeautifulSoup(requst, "html.parser")
all_name = soup.findAll("span", attrs={"class":"title"})
print(all_name)
for name in all_name:
   print(name.string)
