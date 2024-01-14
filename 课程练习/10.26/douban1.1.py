import requests
from bs4 import BeautifulSoup

def mian():
    # 1.获取数据
    get_data()

    # 3.保存数据
    pass

def get_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"
    }
    base_ur1 = "https://movie.douban.com/top250?start=0"
    html1 = requests.get(base_ur1, headers=headers)
    yuan_ma = html1.text
    print(yuan_ma)
    return yuan_ma






if __name__=="__main":
    mian()