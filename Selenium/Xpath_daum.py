from selenium import webdriver
import time
from selenium.webdriver.common.by import By 


driver = webdriver.Chrome(executable_path='/home/rapa01/Documents/Develop/chromedriver')
driver.get(url = "http://www.daum.net")

search_form = driver.find_element(By.TAG_NAME, "form")
search_box = search_form.find_element(By.NAME, "q")
search_box.send_keys("딥러닝")

elements = driver.find_elements(By.XPATH, '//a[@href]')

for e in elements:
    if e !=None:
        print(type(e.text), repr(e.text))
        
driver.quit()
