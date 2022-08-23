#字典
tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print(tinydict['name'])
tinydict={1:100,2:200}
print(tinydict[1])
#修改字典
tinydict={'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
tinydict['Age'] = 8#修改值
tinydict['School']="rookie_like"#增加
del tinydict['School']#删除
print(tinydict)


#字典里的函数
#items() values() keys() claer() pop() popitem() update() fromkeys()
for i in tinydict.items():
    print(i)

for key,value in tinydict.items():
    print(key,value)

re = tinydict.keys()
print(re)
re = tinydict.values()
print(re)
print('*'*30)
result = tinydict.pop('Age','没找到')

print(result)
print('*'*30)

result = tinydict.popitem()#随机删除，一般位最后一个
print(result)

#由于字典不能直接加，可以用update代替
dict1 = {0:100,1:200,2:300}
dict2 = {3:500,4:700}
dict1.update(dict2)#在后面接上dict2
print(dict1)

print('-'*30)
list1 = ['a','b','c']
new_d = dict.fromkeys(list1,10)#把list1转换位new_d字典，无指定（10）则用none代替
print(new_d)

tinydict.clear()
#同一个键不能出现两次
#键不能改变
#存在内置函数 dict
#dict.clear()/copy()


#字典+列表
user = {}
user['name'] = 'name' 
user['password'] = 'password'

database = []
database.append(user)
