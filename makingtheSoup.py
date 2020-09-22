from bs4 import BeautifulSoup

path = 'datas/sample02.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features = 'lxml')
    print(type(soup), soup)

import requests
res = requests.get('https://movie.naver.com/movie/point/af/list.nhn')
print(res.status_code, res.content)
soup = BeautifulSoup(res.content, features="lxml")
print(type(soup), soup.prettify())
