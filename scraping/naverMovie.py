# scrapping naver movie page 
# https://movie.naver.com/movie/point/af/list.nhn

# 1. bring first page (selector, bs)
# 1-1. number, movie name, review, 
# 2. pagination (at lest 6 pages)

from bs4 import BeautifulSoup 
import time
import requests
import sqlite3

<<<<<<< HEAD
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
=======
for x in range(0, 21):
    # time.sleep(5)
    url = "https://movie.naver.com/movie/point/af/list.nhn?&page={}"
    res = requests.get(url.format(x))
    
    soup = BeautifulSoup(res.content, 'lxml')

    # 번호
    number = soup.select("td.ac.num")
    for num in number:
        print(num.text)

    # 제목
    title = soup.select("a.movie.color_b")
    for tit in title:
        print(tit.string)

    #리뷰, 평점 
    data = soup.select("td.title")
    for rev in data:  
        print(rev.text.split('\n')[5])
    for sco in data:
        print(sco.text.split('\n')[3])

    # 리스트 만들기
    NUMBER = [num.text for num in number]
    TITLE = [tit.text for tit in title]
    REVIEW = [rev.text.split('\n')[5] for rev in data]
    SCORE = [sco.text.split('\n')[3] for sco in data]
    print(NUMBER, TITLE, REVIEW, SCORE)

    # DB
    for moviedata in zip(NUMBER, TITLE, REVIEW, SCORE):
        with sqlite3.connect("sqlite/task01") as con:
            cursor = con.cursor()
            query = """
                insert into TASK01 (NUMBER, TITLE, REVIEW, SCORE)
                values (?,?,?,?)
                """
            cursor.execute(query, moviedata)
        con.commit()
>>>>>>> d64cd8fb61763c9b73a739e692f1d3d1660f9a4d
