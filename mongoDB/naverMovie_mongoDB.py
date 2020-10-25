
from bs4 import BeautifulSoup 
import time
import requests
from pymongo import MongoClient


url = "https://movie.naver.com/movie/point/af/list.nhn?&page=1"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'lxml')
titles = soup.select("a.movie.color_b")
number = soup.select("td.ac.num")

db_url = 'mongodb://192.168.219.116:27017/' # 192.168.219.116
with MongoClient(db_url) as client:   # connnect MongoDB
    moviedb = client['MovieDB']  # get Database
    number = ""
    title =""
    review =""
    
    for title in titles:
        number = number
        title = title.text
        datas = soup.select("td.title")
        review = [rev.text.split('\n')[5] for rev in datas]
        data = {"number":number, "title":title, "review":review}
        info = moviedb.naver.insert_one(data)