import requests
from bs4 import BeautifulSoup
import re
import pymysql

findlink = re.compile('<a href="(.*?)">')
findname = re.compile('<span class="title">(.*?)</span>')
findscore = re.compile('<span class="rating_num" property="v:average">(.*?)</span>')
findbj = re.compile(' +(.+)<br/>')
findbeijing = re.compile(' class="" src="(.*?)" width="100"/>')
#findpicture = re.compile()
def main():
    base_url = "https://movie.douban.com/top250?start="
    # 1.获取数据
    data_list = get_data(base_url)

    # 3.保存数据
    file_name = "./douban1.xls"
    save_data(data_list, file_name)

def get_data(base_url):
    data_list = []
    for i in range(0, 25):
        one_url = base_url+str(i*25)  # 生成要爬取网页的网址
        text = ask_html(one_url)
        print("已爬取第"+str(i+1)+"个网页。")

    # 2.解析数据
        bs = BeautifulSoup(text, "html.parser")
        for item in bs.find_all("div", class_="item"):
            movie = []
            item = str(item)
            print(item)
            link = re.findall(findlink, item)[0]
            movie.append(link)
            name = re.findall(findname, item)[0]
            movie.append(name)
            score = re.findall(findscore, item)[0]
            movie.append(score)
            photo = re.findall(findbeijing, item)[0]
            movie.append(photo)
            bj = re.findall(findbj, item)[0]
#           print(bj)
            movie.append(bj)
            data_list.append(movie)
            print(movie)
    return data_list


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

""" excel = xlwt.Workbook(encoding="utf-8")  # 创建workbook（创建excel）
    sheet = excel.add_sheet("豆瓣top250")  # 创建sheet表
    title=["电影链接","电影名","评分","图片", "背景"]
    for i in title:
        sheet.write(0,title.index(i),i)

    for i in range(0,len(date_list)):
        for j in range(0,len(date_list[i])):
            sheet.write((i+1),j,date_list[i][j])
    excel.save(file_name)"""




if __name__ == "__main__":
    main()