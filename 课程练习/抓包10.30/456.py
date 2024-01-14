import requests
from bs4 import BeautifulSoup
import re

findlink = re.compile('<a href="(.*?)"></a>')
findname = re.compile('<span class="title">(.*?)</span>')
findscore = re.compile('<span class="rating_num" property="v:average">(.*?)</span>')
finddirector = re.compile('<p class>(.*?)</p>')
def zhu():
    base_url = "https://movie.douban.com/top250?start="
    data_list = get_data(base_url)

    file_name = "./douban.xls"
    save_data(data_list, file_name)


def get_data(base_url):
    data_list = []
    for i in range(0, 10):
        one_url = base_url + str(i * 25)
        text = ask_html(one_url)

        bs = BeautifulSoup(text, "html.parser")
        for item in bs.find_all("div", class_="item"):
            data = []
            item = str(item)
            link = re.findall(findlink, item)[0]
            data.append(link)
            name = re.findall(findname, item)
            data.append(name)
            score = re.findall(findscore, item)
            director = re.findall(finddirector, item)
            print(link, name, score, director)
    return data_list


def ask_html(one_url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79"}
    resp = requests.request("GET", one_url, headers=head)
    return resp.content


def ask_html(one_url):
    head = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61"}
    resp = requests.request(method="GET", url=one_url, headers=head)
    return resp.content


def save_data(data_list, file_name):
    pass


if __name__ == "__main__":
    zhu()