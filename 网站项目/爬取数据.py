import requests
from bs4 import BeautifulSoup
#import re
#import pymysql

#findpicture = re.compile()
def main():
    base_url = "https://45maokw.com/"
    # 1.获取数据
    data_list = get_data(base_url)


def get_data(base_url):
        bs = BeautifulSoup(base_url, "html.parser")
        print(bs)



def ask_html(one_url):
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61"}
    resp = requests.request("GET", url=one_url, headers=head)
    return resp.content


if __name__ == "__main__":
    main()