import time
import requests

url = 'https://go.drugbank.com/drugs?page={}'

for x in range(0,5):
    time.sleep(5)
    re = requests.get(url.format(x))
    print(url.format(x))
    print(re)

# for x in range(0,107):
#     time.sleep(5)
#     re = requests.get(url.format(x))
#     print(url.format(x))
#     print(re)

