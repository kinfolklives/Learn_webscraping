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



con = soup.select("#container")
# number
number = soup.select("td.ac.num")
for n in number:
    st = n.string 
    print(st)
# title
# review
# score

movie_data = soup.select("td.title")[0]
for title in movie_data:
    title = movie_data.text.split('\n')[1]

# for title in movie_data:
#     title = movie_data.text.split('\n')[1]
#     review = movie_data.text.split('\n')[3]
#     score = movie_data.text.split('\n')[5]
#     data.append(title)
#     print(data)

# with sqlite3.connect("test02") as con:
#     cur = con.cursor()
#     NUMBER =""

#     query = """
#     insert into TEST01 (NUMBER) values (?)
#     """
#     for num in number:
#         NUMBER = st
        
    #         cur.execute(query, (NUMBER, TITLE, REVIEW, SCORE))
    #     con.commit()




    

#url = 'https://go.drugbank.com/drugs?page={}'