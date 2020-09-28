from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/rapa01/Documents/Develop/chromedriver')
print(type(driver), driver)

driver.get(url="http://google.com")
print(type(driver.page_source), driver.page_source)

driver.quit()

