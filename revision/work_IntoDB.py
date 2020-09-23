from bs4 import BeautifulSoup
import requests
import sqlite3

res = requests.get("https://www.google.com/search?q=%EC%B7%A8%EC%97%85+%EC%82%AC%EC%9D%B4%ED%8A%B8&oq=%EC%B7%A8%EC%97%85+%EC%82%AC%EC%9D%B4%ED%8A%B8&aqs=chrome..69i57j69i60j69i61j69i60.5524j0j15&sourceid=chrome&ie=UTF-8")
soup = BeautifulSoup(res.content, features="lxml")

print(div)
# for a in  body.find_all("a", class_="fohFr"):
#     print(a)

# links = soup.select('p[id]')
# with sqlite3.connect("db.sqlite3") as con:
#         cur = con.cursor()
#         title = ""
#         link = ""
#         query = """
#         insert into sample03 (title,link,create_date) values (?,?,datetime('now'))
#         """
#         for link in links:
#             title = str.strip(link.get_text())
#             link = link['id']
#             cur.execute(query, (title, link))
#         con.commit()