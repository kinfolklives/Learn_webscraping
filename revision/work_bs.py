from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.google.com/search?q=%EC%B7%A8%EC%97%85+%EC%82%AC%EC%9D%B4%ED%8A%B8&oq=%EC%B7%A8%EC%97%85+%EC%82%AC%EC%9D%B4%ED%8A%B8&aqs=chrome..69i57j69i60j69i61j69i60.5524j0j15&sourceid=chrome&ie=UTF-8")
soup = BeautifulSoup(res.content, features="lxml")

# siblings
h2p = soup.body.h2.parent
for sibling in h2p.next_siblings:
    print(type(sibling.a), sibling.a)
    print("-"*50)
# referenced from joon-hee

# find
body = soup.body
for a in  body.find_all("a", class_="fohFr"):
    print(a)
    print("-"*50)

    