# scrapping naver movie page 
# https://movie.naver.com/movie/point/af/list.nhn

# 1. bring first page (selector, bs)
# 1-1. number, movie name, review, 
# 2. pagination (at lest 6 pages)

from bs4 import BeautifulSoup 
import time
import requests
import sqlite3

res = requests.get('https://movie.naver.com/movie/point/af/list.nhn')
soup = BeautifulSoup(res.content, 'lxml')
# number
number = soup.select("td.ac.num")
for num in number:
    print(num)
# print(type(number), number.string) # e.tag

# movie name
m_title = soup.select("a.movie.color_b")
for t in m_title:
    print(t.string)
#print(type (m_name), m_name.get_text()) # e.tag

# review 2
review = soup.select(".list_netizen > tbody:nth-child(4) > tr:nth-child(4) > td:nth-child(2)")[0]
print(review.text.split('\n')[5])



#url = 'https://go.drugbank.com/drugs?page={}'