from pymongo import MongoClient
from bs4 import BeautifulSoup

path = 'datas/sample03.html'
db_url = 'mongodb://192.168.219.116:27017/' # 192.168.219.116
    with MongoClient(db_url) as client:   # connnect MongoDB
        sampledb = client['sample03db']  # get Database
        title=''
        link =''
        for link in links:
            title = str.strip(link.get_text())
            link = link['id']
            data = {'title':title, 'id':link}
            info = sampledb.naver.insert_one(data)