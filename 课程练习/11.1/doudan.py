import requests
from bs4 import BeautifulSoup
import re
import xlwt


findname=re.compile('<span class="title">(.*?)</span>')
findscore = re.compile('<span class="rating_num" property="v:average">(.*?)</span>')

def main():
    base_ur1="https://movie.douban.com/top250?start="
#1.获取数据
    data_list=get_data(base_ur1)
#3.保存数据

    file_name="./douban.xls"
    save_data(data_list,file_name)

def get_data(base_url):
    data_list=[]
    for i in range(0,25):
        one_url=base_url+str(i*25)
#生成要爬取网页的网址text=ask html(one url)print("已爬取第"+str(i+1)+"个网页。")
        text = ask_html(one_url)
        print("已爬取第" + str(i + 1) + "个网页。")

        # 2.解析数据
        bs = BeautifulSoup(text, "html.parser")
        for item in bs.find_all("div", class_="item"):
            data = []
            item = str(item)
            print(item)
            name = re.findall(findname, item)[0]
            data.append(name)
            #link = re.findall(findlink, item)[0]
            #data.append(link)

            score = re.findall(findscore, item)[0]
            data.append(score)
            data_list.append(data_list)
            #director = re.findall(finddirector, item)
            #print(link, name, score, director)
            data_list.append(data)
            print(data)
    print(data_list)
    return data_list

def ask_html(one_url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76"}
    resp = requests.request(method="GET", url=one_url, headers=head)
    return resp.content

def save_data(data_list, file_name):
    excel = xlwt.Workbook(encoding="utf-8")  # 创建workbook(创建excel)
    sheet = excel.add_sheet("豆瓣top25")  # 创建sheet表
    title = ["电影名", "电影链接"]
    for i in title:
        sheet.write(0, title.index(i), i)

    for i in range(0, len(data_list)):
        for j in range(0, len(data_list[i])):
            sheet.write((i + 1), j, data_list[i][j])
    excel.save(file_name)

if __name__ == "__main__":
    main()