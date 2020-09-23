import requests
from bs4 import BeautifulSoup
res = requests.get('http://media.daum.net/economic/')
print(res.status_code, res.content)
soup = BeautifulSoup(res.content, 'lxml')
links = soup.select("a[href]")
for link in links:
    print(type(link), link)    
