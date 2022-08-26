#urllib / requests

#requests:python 中原生基于网络请求的模块,模拟浏览器发送请求

#使用：
#1.指定url
#2.发送请求
#3.获取响应数据
#4.持续化存储
import requests
import json

#初尝试
def f1():
    url = "https://www.sogou.com/"
    res = requests.get(url = url,)
    page_text = res.text#没有括号！！且text为原本的内容，content为加载后的内容
    print(page_text)

    with open('./sohou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("over!!")



#简易的网页采集器
def f2():
    #UA伪装：
    #网址服务器会检测对于请求的载体的ua，如果为某一浏览器，则正常通过
    #否则判断为爬虫，服务器可能拒绝通过


    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
        #身份标识
    }
    url = 'https://www.sogou.com/web?query=%E6%B3%A2%E6%99%93%E5%BC%A0'
    #url中 %E6%B3%A2%E6%99%93%E5%BC%A0 为我使用搜索引擎的需求，可以进行更改
    #即处理url携带的参数
    kw = input("输入关键词:")
    param = {
        'query':kw
    }
    url = 'https://www.sogou.com/web'
    res = requests.get(url = url,params = param,headers = headers)
    #即在url中参数为param

    page_text = res.text

    filename = kw+'.html'
    with open('./'+filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("over!!")



#翻译页面破解
def f3():
    kw = input("请输入关键字:")

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
    }

    #post请求非get ， 且携带参数
    #响应数据为json数据
    url = 'https://fanyi.baidu.com/sug'
    
    #在负载里看keyword
    data = {
        'kw' : kw
    }
    res = requests.post(url = url,data=data,headers = headers)
    dec_obj = res.json()#返回的是obj
    print(dec_obj)

    filename = kw+'.json'
    fp = open('./'+filename,'w',encoding='utf-8')
    json.dump(dec_obj,fp,ensure_ascii=False)
    print('over!!!')


if __name__ == '__main__':
    f3()
