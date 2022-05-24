import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'#小说类
web_data = requests.get(url,headers = headers)
soup = BeautifulSoup(web_data.content,'html.parser')

title = soup.select('h2')
author = soup.select('div.pub')
score = soup.select('span.rating_nums')
introduction = soup.select('div.info>p')
photo = soup.select('img')

for x,y,z,m,n in zip(title,author,score,introduction,photo):
    title = x.get_text().strip('\n /')
    author = y.get_text().strip('\n /')
    score = z.get_text().strip('\n /')
    introduction = m.get_text().strip('\n /')
    photo_src = n.get('src')
    data = {
        '标题':title,
        '作者':author,
        '评分':score,
        '简介':introduction,
        '图片链接':photo_src
    }
    print(data)
