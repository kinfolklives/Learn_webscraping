import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.google.com/search?rlz=1C1SQJL_koKR912KR912&sxsrf=ALeKk01NcS50KLE8PnOScdcUVFKmk37qCw%3A1600752583318&ei=x4tpX6SBE4TbhwP65qPQDA&q=%EC%B7%A8%EC%97%85&oq=%EC%B7%A8%EC%97%85&gs_lcp=CgZwc3ktYWIQAzIFCAAQsQMyBAgAEEMyBAgAEEMyBQgAELEDMgQIABBDMgIIADICCAAyAggAMgIIADICCABQ1yhYvixg3y1oAXABeAGAAX-IAdMFkgEDMC42mAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwjkgOiIhPzrAhWE7WEKHXrzCMoQ4dUDCA0&uact=5")
soup = BeautifulSoup(res.content, 'html.parser')
links = soup.select('a')
print(type(links), len(links))		
#print(links)
for link in links:
    print(type(link),link)      
    print('-'*100)