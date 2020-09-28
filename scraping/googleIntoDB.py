from bs4 import BeautifulSoup
import requests
import sqlite3

res = requests.get("https://www.google.co.kr/search?safe=active&sxsrf=ALeKk02ew3ZOBjQoDqdTHjgeR8PLzDPMNQ%3A1600869558971&source=hp&ei=tlRrX8D5OM34wAOd3pzYAg&q=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&oq=&gs_lcp=CgZwc3ktYWIQARgBMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGC1EmgBcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQo&sclient=psy-ab")
soup = BeautifulSoup(res.content, features="lxml")


div = soup.body.