from bs4 import BeautifulSoup
import requests

res = requests.get("https://search.naver.com/search.naver?f=&fd=2&filetype=0&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&query=%EC%B7%A8%EC%97%85+%EC%82%AC%EC%9D%B4%ED%8A%B8&research_url=&sm=tab_nmr&start=1&where=webkr")
soup = BeautifulSoup(res.content, features="lxml")

s = soup.find_all(class_="title_link", attrs={"href":True})
print(s)
