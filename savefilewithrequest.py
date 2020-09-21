import requests
url = 'http://blog.naver.com/otter35'
url = 'http://www.coupang.com'
header = {'User-Agent':""}   # 알아가기 참조 
res = requests.get(url=url, headers=header)
print(type(res), res) #<class 'requests.models.Response'><Response[200]>
if(res.status_code == 200):
    with open('datas/response01.html', 'w') as fp:
        fp.write(res.text)
