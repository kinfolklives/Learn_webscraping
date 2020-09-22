from bs4 import BeautifulSoup
import requests

with open('datas/sample02.html') as fp:
    soup = BeautifulSoup(fp, features='lxml')

# Going sideways- .next_sibling and .next_siblings
link = soup.a
print(type(link.next_sibling), link.next_sibling)

print(type(link.next_sibling.next_sibling), link.next_sibling.next_sibling)

# for sibling in soup.a.next_siblings:
#     print(type(sibling), repr(sibling)) # return a printable representation 



