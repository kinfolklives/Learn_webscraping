from bs4 import BeautifulSoup 

with open('datas/sample02.html') as fp:
    soup = BeautifulSoup(fp, features='lxml')

    