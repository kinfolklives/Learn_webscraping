# "네이버를 시작페이지로"
# 뉴스기사 links 수집

from bs4 import BeautifulSoup
import requests

res = requests.get("https://naver.com")
soup = BeautifulSoup(res.content, features="lxml")

body = soup.body
name = body.find("a", id="NM_set_home_btn")
print(name.string)


