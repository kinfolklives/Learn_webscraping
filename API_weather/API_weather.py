import requests
import json
import sqlite3
import time 
# 1. 데이터 열기 + 읽어오기
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
apikey = '15a69c44009dea19b327ba81ecb4d2b7'
# cities = "london" # 1. 도시이름 나열? 2. json 파일 이용해서 가져오기?
with open("citylist.json", 'rt', encoding='UTF8') as citylist:
    clist = json.load(citylist)

cityList = []
mainList = []
descList = []
tempList =[]
feelsList =[]
humList = []
for i in range(0,31):
    time.sleep(1)
    # 2. 원하는 정보 얻기 (city)
    cities = clist[i]['name']
    cities = cities
    # print(type(cities), cities)
    cityList.append(cities)

    res = requests.get(url.format(cities,apikey))
    if res.status_code == 200:
        rt_dict = json.loads(res.content)

    # 2. 원하는 정보 얻기 (current weather)
    main = rt_dict['weather'][0]['main']
    desc = rt_dict['weather'][0]['description']
    temp = rt_dict['main']['temp']
    feels = rt_dict['main']['feels_like']
    hum = rt_dict['main']['humidity']
    
    # 3. 리스트만들기
    mainList.append(main)
    descList.append(desc)
    tempList.append(temp)
    feelsList.append(feels)
    humList.append(hum)

    # 4. DB 저장 
    for weatherdata in zip(cityList, mainList, descList, tempList, feelsList, humList):
        print(weatherdata)
        # with sqlite3.connect("") as con:
        #     cursor = con.cursor()
        #     query = """
        #         insert into TASK01 ()
        #         values (?,?)
        #         """
        #     cursor.execute(query, weatherdata)
        # con.commit()


    