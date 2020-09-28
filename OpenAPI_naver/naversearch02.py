import sqlite3
import requests
import os
import sys
import urllib.request
import json

client_id = "s87lXXkMwUFgwYj6GdXq"
client_secret = "_TSjaqPXh4"
encText = urllib.parse.quote("커피")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText 
# url = ”https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

with urllib.request.urlopen(request) as result:
    data = json.loads(result.read().decode('utf8'))
    print(type(data), data.keys())
    # dict_keys(['lastBuildDate', 'total', 'start', 'display', 'items']) 
    # lastBuildDate/ items - title, link, 
    
    date = data['lastBuildDate']
    title = data['items'][0]['title']
    link = data['items'][0]['link']
    print(type(title))
    # rescode = response.getcode()
    # print(rescode)

    naverdate = []
    navertitle = []
    naverlink = []
    naverdate.append(date)
    navertitle.append(title)
    naverlink.append(link)
    
# 4. DB 저장 
for naverdata in zip(naverdate, navertitle, naverlink):
    # print(naverdate)
    with sqlite3.connect("/home/rapa01/Documents/Develop/learn_webscraping/sqlite/db.choi") as con:
        # print(naverdata)
        cursor = con.cursor()
        query = """
            insert into NaverAPI (date, title, link)
            values (?,?,?)
            """
        cursor.execute(query, naverdata)
    con.commit()