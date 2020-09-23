import requests

# url = 'http://blog.naver.com/otter35'
url = 'https://www.coupang.com'
header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}   # 알아가기 참조 
# https://www.whatismybrowser.com/detect/what-is-my-user-agent 
res = requests.get(url=url, headers=header)
print(type(res), res) 
#<class 'requests.models.Response'><Response[200]>

print(res.status_code)
if(res.status_code == 200):
    with open('datas/response01.html', 'w') as fp: # vs code 는 파일의 폴더가 root로 인식. 그래서 datas/resposes01.html 
        fp.write(res.text)
