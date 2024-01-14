from bs4 import BeautifulSoup
import requests
import re
findd = re.compile('<img alt=(.*?) class="" src="(.*?)" width="100"/>')
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"
}
response = requests.get("https://45maokw.com/maoplay/281072_1_1.html", headers = headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")
#print(soup)
all_name = soup.findAll("img", attrs={"id":"video"})
print(all_name)
"""    for name in all_name:
        title = name.string
        if "/" not in title:
            print(title)"""





#document (https://45maokw.com/static/player/dplayer.html)