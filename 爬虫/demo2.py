import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.baidu.com")
print(resp)

print(resp.content)
print('-'*30)

bsobj = BeautifulSoup(resp.content,'lxml')
print(bsobj)

a_list = bsobj.find_all('a')
for a in a_list:
    print(a.get('href'))