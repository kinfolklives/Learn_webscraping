from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/rapa01/Documents/Develop/chromedriver')

driver.get(url = "http://www.google.com")
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

SearchInput = driver.find_element(By.NAME, 'q')
SearchInput.send_keys("selenium")

SearchInput.clear()