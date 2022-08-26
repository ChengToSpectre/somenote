import requests
import json

def f():
    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
        #身份标识
    }
    res = requests.get(url = url,headers  = header).text

if __name__ == '__main__':
    f()