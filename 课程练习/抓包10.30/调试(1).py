import requests
from bs4 import BeautifulSoup
import csv
 
'''爬取豆瓣电影top20'''
def top250_crawer(url,sum):
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/1'
 
    }
 
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movie_items = soup.find_all('div', class_='item')
    i = sum+1
    for item in movie_items:
         title = item.select_one('.title').text
         
         rating = item.select_one('.rating_num').text
         data = item.select('.bd p')[0].text.split('\n')
         time = data[2].replace(' ','').split('/')[0]
         country = data[2].replace(' ','').split('/')[1]
         print(str(i)+'.'+title+','+country+','+time)
 
         i +=1
 
url = 'https://movie.douban.com/top250'
sum =0
'遍历10页数据，250条结果'
for a in range(10):
    if sum == 0 :
        top250_crawer(url,sum)
        sum +=25
    else:
        page = '?start='+str(sum)+'&filter='
        new_url = url+page
        top250_crawer(new_url,sum)
        sum +=25