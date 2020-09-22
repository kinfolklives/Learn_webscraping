from bs4 import BeautifulSoup
import requests

with open('datas/sample02.html') as fp:
    soup = BeautifulSoup(fp, features='lxml')

print(type(soup.find(id='link3')), soup.find(id="link3"))
