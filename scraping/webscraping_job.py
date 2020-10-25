from bs4 import BeautifulSoup 
import requests
import sqlite3

res = requests.get("https://www.jobkorea.co.kr/")
soup = BeautifulSoup(res.content, features="lxml")

# vvip 채용관 업체명 가져오기 

