import requests
import json

# 1. 데이터 가져오기 
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
apikey = '15a69c44009dea19b327ba81ecb4d2b7'
# citynames = "london" # 1. 도시이름 나열? 2. json 파일 이용해서 가져오기?
with open("citylist.json") as citylist:
    citylist = json.load(citylist)
    clist = clist[0]['id'] for clist in citylist
    print(clist)

res = requests.get(url.format(clist,apikey))
rt_dict = json.load(res.content)
# print(rt_dict, rt_dict.keys())

# 2. 원하는 정보 얻기 (city/ current weather)
city = rt_dict['name']
# print(type(city),city)
current_weather = rt_dict['weather']
# print(type(current_weather))
c_weather = current_weather[0]['main']
print(c_weather)

# 3. DB 저장 
