import wget
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/rapa01/Documents/Develop/chromedriver')
url = "https://www.coupang.com/np/search?q=컴퓨터" # as HTTP 200
driver.get(url=url)
elements = driver.find_elements(By.XPATH, '//img[@class="search-product-wrap-img"]')
down_path='/home/rapa01/Pictures/'
for element in elements:
    src = element.get_attribute('src')
    # print(src)
    # download the image
    img_txt = src.split('/')[-1]
    image_name = down_path + img_txt
    
    # first way
    # wget.download(url=src, out=image_name) # HTTP Error 403: Forbidden
    
    # second way 
    # dowload the file from 'url' and save it locally under 'file_name':
    with urllib.request.urlopen(src) as response, open(image_name, 'wb') as out_file:
        data = response.read() # a 'bytes' object
        out_file.write(data)
        
# https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/2020/04/14/11/7/
# 5fffe9f5-c0b2-4e33-be1b-38fce958add5.jpg
# 94c47901a19340faef17180c4d31dfdc488a56c959b3b175fdc9938cfb2a.png