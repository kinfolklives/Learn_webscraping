import requests
from bs4 import BeautifulSoup

path= 'datas/sample02.html'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    a = soup.select(selector='title')
    print(type(a), a)

    a = soup.select("body a") # body 아래 a 모두
    print(type(a), a)

    a = soup.select("head > title")  # head 아래 타이틀만 
    print(type(a), a)

    a = soup.select("p > a") # p 아래 a 모두
    print(type(a), a)

    a = soup.select("p > #link1") # p아래 id=link1 , # : id 
    print(type(a), a)

    a = soup.select("#link1~.sister") # ~ : siblings, . : class 
    print(type(a), a)

    a = soup.select(".sister")
    print(type(a), a)

    a = soup.select("[class~=sister]")
    print(type(a), a)

    a = soup.select("a#link2")
    print(type(a), a)

    a = soup.select('a[href]') # a 아래 href 모두 
    print(type(a), a)

    a = soup.select('a[href^="http://example"]')
    print(type(a), a)

    a = soup.select('a[href*=".com/el"]')
    print(type(a), a)

    

