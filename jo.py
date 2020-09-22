import requests
from bs4 import BeautifulSoup
import bs4

# find_all을 이용하여 취업사이트 주소 가져오기
def find_a_using_findAll(soup):
    divs = soup.find_all('div', class_= 'r')
    for div in divs:
        print(div.a)

def find_a_using_pcs(soup):
    h2_tag = soup.body.h2
    # print(list(h2_tag.parent.next_siblings))
    for sibling in h2_tag.parent.next_siblings:
        print(sibling.a)

# 헤더 파일 필요 (https://www.whatismybrowser.com/detect/what-is-my-user-agent 에서 검색)
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
url = '''
    https://www.google.com/search?q=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&oq=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&aqs=chrome..69i57j0l7.6250j0j15&sourceid=chrome&ie=UTF-8
    '''
res = requests.get(url, headers=header)

if res.status_code==200:
    soup = BeautifulSoup(res.content, features='lxml')
    print('='*100)
    find_a_using_pcs(soup)
    print('='*100)
    find_a_using_findAll(soup)
    print('='*100)