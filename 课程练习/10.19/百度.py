import requests
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188"
}
def mian():
    base_url = "https://movie.douban.com/top250?start="

    get_data(base_url)
    pass

def get_data(base_url):
    for i in range(1,11):
        final_url = base_url+str((i-1)*25)
        print(final_url)
        html1 = requests.get(final_url, headers=headers)
        print(html1.text)
        bao_cun(html1)

def bao_cun(html1,):
    with open("douban.html", "wb") as f:
        f.write(html1.content)




if __name__=="__main__":
    mian()