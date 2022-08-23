import os
import requests
from bs4 import BeautifulSoup

file = "D:\pyhton\demo\爬虫"

def mkdir(path):
 
	folder = os.path.exists(path)#path为路径
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("---  new folder...  ---")
		print("---  OK  ---")
 
	else:
		print("---  There is this folder!  ---")

mkdir(file)

res = requests.get("https://www.baidu.com")

print(res)
#print(res.content)

bso = BeautifulSoup(res.content,'lxml')
a_list = bso.find_all('a')

text = ''
for a in a_list:
    href = a.get('href')
    text += href+'\n'


with open('url.txt','w') as f:
    f.write(text)