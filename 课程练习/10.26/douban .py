import requests
from bs4 import BeautifulSoup

def main():
    beas_url = "https://movie.douban.com/top250?start="
    data_list = get_data(beas_url)
    file_name = "./douban.xls"
    save_data(data_list,file_name)


'''def get_data(beas_url):
    data_list = []
    for i in range(0,25):
        one_url = beas_url+str(i*25)#获取王谢
        demo_html = ask_html(one_url)
        bs = BeautifulSoup(str(demo_html), "html.parser")
        print(bs.findAll("div", attrs={"class": "item"}))

        #解析数据
    return data_list
''''def ask_html(one_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"
    }
    resp = requests.get(one_url, headers=headers)
    print(resp)
    return resp
def save_data(data_list,file_name):#保存数据
    pass

if __name__=="__main__":
    main()