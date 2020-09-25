from bs4 import BeautifulSoup 
import time
import requests
import sqlite3

info_url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"

res = requests.get(info_url)
soup = BeautifulSoup(res.content, 'lxml') 

# locations = soup.find_all('location')
# for location in locations:
#     print(location.find('city').text, ":", location.find('wf').text)

locations = soup.select('location')
print(type(locations))
for location in locations:
    print(location.find('city').text, ":", location.find('wf').text)