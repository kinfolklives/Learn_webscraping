from bs4 import BeautifulSoup 
import sqlite3

path = 'datas/sample03.html'
with open(path, 'rt', encoding='UTF8') as fp:
    soup= BeautifulSoup(fp, features='lxml')
    links = soup.select('p[id]')
    with sqlite3.connect("db.sqlite3") as con:
        cur = con.cursor()
        title = ""
        link = ""
        query = """
        insert into sample03 (title,link,create_date) values (?,?,datetime('now'))
        """
        for link in links:
            title = str.strip(link.get_text())
            link = link['id']
            cur.execute(query, (title, link))
        con.commit()
