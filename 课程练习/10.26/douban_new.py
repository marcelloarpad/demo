import requests
from bs4 import BeautifulSoup
import re

findlink=re.compile('')
findname=re.compile('')

def main():
    base_ur1="https://movie.douban.com/top250?start=0=0"
    #1.获取数据
    data_list=get_data(base_ur1)

    #3.保存数据
    file_name="./douban.xls"
    save_data(data_list,file_name)

def get_data(base_ur1):
    data_list=[]
    for i in range(0,25):
        one_ur1=base_ur1+str(i*25)   #生成要爬取网页的网址
        text=ask_html(one_ur1)

    #2.解析数据
    bs=BeautifulSoup(text,"html.parser")
    for item in bs.find_all("div",class_="item"):
        item=str(item)
        link=re.findall(findlink,item)[0]
        name=re.findall(findname.item)[0]
        print(name)

    return data_list

def ask_html(one_ur1):
    head={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188}"
    }
    resp=requests.request("GET",ur1=one_ur1,headers=head)
    return resp.content

def save_data(data_list,file_name):
    pass

if __name__=="__main__":
    main()