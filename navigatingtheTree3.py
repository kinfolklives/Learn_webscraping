from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.google.com/search?sxsrf=ALeKk03iw1Oow586L9OL8Bn6on-zu6OwcQ%3A1600752835436&ei=w4xpX-6cGqPEmAWv5IWwCg&q=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&oq=%EC%B7%A8%EC%97%85%EC%82%AC%EC%9D%B4%ED%8A%B8&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgw5rPAmgAcAF4AIABAIgBAJIBAJgBAKoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwiuioSBhfzrAhUjIqYKHS9yAaYQ4dUDCA0&uact=5")
soup = BeautifulSoup(res.content, features="lxml")

link = soup.a
print(link)
for sibling in link.next_siblings:
    print(type(sibling), sibling)

