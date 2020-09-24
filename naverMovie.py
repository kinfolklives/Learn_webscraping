# scrapping naver movie page 
# https://movie.naver.com/movie/point/af/list.nhn

# 1. bring first page (selector, bs)
# 1-1. number, movie name, review, 
# 2. pagination (at lest 6 pages)

from bs4 import BeautifulSoup 
import time
import requests
import sqlite3

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
<<<<<<< HEAD
    print(NUMBER, TITLE, REVIEW, SCORE)

    # DB
    for moviedata in zip(NUMBER, TITLE, REVIEW, SCORE):
        with sqlite3.connect("sqlite/task01") as con:
            cursor = con.cursor()
            query = """
                insert into TASK01 (NUMBER, TITLE, REVIEW, SCORE)
=======
    #print(NUMBER, TITLE, REVIEW, SCORE)

    for moviedata in zip(NUMBER, TITLE, REVIEW, SCORE):
        with sqlite3.connect("test02") as con:
            cursor = con.cursor()
            query = """
                insert into TEST01 (NUMBER, TITLE, REVIEW, SCORE)
>>>>>>> 034b7941fbf07cb35abeac4376cf0a1d872f2d81
                values (?,?,?,?)
                """
            cursor.execute(query, moviedata)
        con.commit()
