# "네이버를 시작페이지로"
# 뉴스기사 links 수집

from bs4 import BeautifulSoup
import requests

res = requests.get("https://naver.com")
soup = BeautifulSoup(res.content, features="lxml")

# body = soup.body
# name = body.find("a", id="NM_set_home_btn")
# print(name.string)


# links 수집 
# 1. 특정 div 가져오기(find), 그중 class="sc_themecast id_health"
# 2. find_all("a")

div = soup.find("div", class_="list_theme_wrap")
print(div, "-----")
a_tag = div.find_all("a")


