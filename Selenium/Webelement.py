from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/rapa01/Documents/Develop/chromedriver')

driver.get(url = "http://www.google.com")
from selenium.webdriver.common.by import By 
search_form = driver.find_element(By.TAG_NAME, "form")
print(type(search_form), search_form)

search_box = search_form.find_element(By.NAME, "q")
search_box.send_keys("webdriver")

print(search_box)