from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.google.com/search?q=%EC%B7%A8%EC%97%85+%EC%82%AC%EC%9D%B4%ED%8A%B8&oq=%EC%B7%A8%EC%97%85+%EC%82%AC%EC%9D%B4%ED%8A%B8&aqs=chrome..69i57j69i60j69i61j69i60.5524j0j15&sourceid=chrome&ie=UTF-8")
soup = BeautifulSoup(res.content, features="lxml")

link = soup.a
print(type(link), link)
for sibling in link.next_siblings:
    print(type(sibling), sibling)

