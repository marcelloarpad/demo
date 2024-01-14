import requests
from bs4 import BeautifulSoup
import re
import pymysql

"""findlink = re.compile('<a href="(.*?)">')
findname = re.compile('<span class="title">(.*?)</span>')
findscore = re.compile('<span class="rating_num" property="v:average">(.*?)</span>')
findbj = re.compile(' +(.+)<br/>')
findbeijing = re.compile(' class="" src="(.*?)" width="100"/>')"""
#findpicture = re.compile()
def main():
    base_url = "https://we.51job.com/pc/search?jobArea=250200&keyword=%E7%BD%91%E7%BB%9C&searchType=2&degree=03&sortType=0&metro="
    data_list = get_data(base_url)
    print(data_list)

def get_data(base_url):
    one_url =base_url   # 生成要爬取网页的网址
    text = ask_html(one_url)
    # 2.解析数据
    bs = BeautifulSoup(text, "html.parser")
    return bs
def ask_html(one_url):
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61"}
    resp = requests.request("GET", url=one_url, headers=head)
    return resp.content

def save_data(date_list, file_name):
    db = pymysql.connect(host="localhost", user="root", password="123456", database="douban", port=3306)
    cursor = db.cursor()
    for movie in date_list:
        sql = f"insert into doubantop250 values('{movie[0]}', '{movie[1]}', '{movie[2]}', '{movie[3]}', '{movie[4]}');"
        cursor.execute(sql)
        db.commit()
    db.close()

if __name__ == "__main__":
    main()