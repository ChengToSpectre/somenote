# 爬取豆瓣电影/kfc
# 页面局部更新

import json
import requests
import string

null=None

def f1():
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',  #从第几部电源开始选,电影为第0个开始
        'limit': '20'   #一次请求取出的个数
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
        #身份标识
    }
    res = requests.get(url = url,params = param,headers = headers)
    list_data = res.json()

    with open('./douban.json','w',encoding='utf-8') as fp:
        json.dump(list_data,fp,ensure_ascii=False)
    print("over!!!!")



def f2():
    kw = input("Enter the keywords:")
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
        #身份标识
    }
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    flag = 1
    sign = 1
    number_pages = 0
    while flag:
        number_pages += 1
        data = {
            'cname': '',
            'pid': '',
            'keyword': kw,
            'pageIndex': number_pages,
            'pageSize': '10'
        }
        res = requests.post(url = url,data = data,headers = header)
        #内容形式为Content-Type: text/plain; charset=utf-8
        #非json
        text = res.text
        print(text)
        directory = eval(text)
        if directory['Table1'] == []:
            break
        filename = 'address'+'.txt'
        fp = open('./'+filename,'a',encoding='utf-8')
        fp.write(text)
    print('over!!!')




def f3():
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    # UA伪装
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
        #身份标识
    }
    word = input("请输入地址: ")
    numbers = 1
    # 页数
    number_pages = 0
    # 第一次检测页数
    state = True
    while numbers != 0:
        number_pages += 1
        data = {
            'cname': '',
            'pid': '',
            'keyword': word,
            'pageIndex': number_pages,
            'pageSize': '10',
        }
        response = requests.post(url=url, data=data, headers=header)
        text = response.text
        numbers -= 1
        # 计算页数,因为只需要一次即可
        if state:
            # 将列表text转化为字典
            dictionary = eval(text)
            # 获取第一段Table的页数
            rowcount = dictionary['Table']
            # 将这个列表中的字典赋给dicts
            dicts = rowcount[0]
            # 查询rowcount所指的页数
            numbers = dicts['rowcount']
            if numbers == 0:
                print("抱歉,您所输入的地址没有肯德基餐厅")
            else:
                print(f"{word}一共有{numbers}家肯德基餐厅")
            if numbers % 10 == 0:
                numbers = numbers // 10
            else:
                numbers = numbers // 10  # 不加一是因为已经检查过一次了
            state = False

        print(text)

if __name__ == '__main__':
    f2()