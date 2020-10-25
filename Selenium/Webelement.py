from selenium import webdriver
driver = webdriver.Chrome('/home/rapa01/Documents/Develop/chromedriver'): # 드라이버 경로지정, 불러오기 
driver.get(url = "http://www.google.com") # driver.get(url) : url 불러오기 

from selenium.webdriver.common.by import By
search_form = driver.find_element(By.TAG_NAME, "form") # Tag 찾기 : TAG_NAME > 크롬 써치박스 tag 
# print(type(search_form), search_form)

search_box = search_form.find_element(By.NAME, "q") # Tag로 찾은 것에서 name='q' > 크롬 서치박스 tag > name 
search_box.send_keys("webdriver") # send key 

elements = driver.find_elements(By.XPATH, '//a[@href]') # XPATH 로 찾기 
print(type(elements), elements)

for e in elements:
    if e !=None:
        print(type(e.text), repr(e.text))
        
driver.quit()

