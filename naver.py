from bs4 import BeautifulSoup
import requests

res = requests.get("https://naver.com")
soup = BeautifulSoup(res.content, features="lxml")

# "네이버를 시작페이지로"
body = soup.body
name = body.find("a", id="NM_set_home_btn")
print(name.string)

# links 수집 
# 1. 특정 div태그 가져오기(find), class="class="theme_cont" 
# 2. a태그 가져오기

div = soup.find("div", class_="theme_cont")
for a in div.find_all("a"):
    print(type(a), a)
    print("-"*100)