# s= 'jdlkajsldjlkashlf'
# myli = iter(s)
# print(next(myli))

# class num:
#     def __iter__(self):
#         self.a = 1
#         return self
        
#     def __next__(self):
#         if self.a < 10:
#             x = self.a
#             self.a += 1
#             return x
#         else :
#             raise StopIteration#停止

# my = num()
# myiter = iter(my)

# for i in myiter:
#     print(i)

# import mymodule

# mymodule.greeting("Bill")

import datetime

x = datetime.datetime.now()

print(x)    


import json

# 一些 JSON:
x =  '{ "name":"Bill", "age":63, "city":"Seatle"}'

# 解析 x:
y = json.loads(x)

# 结果是 Python 字典：
print(y["age"])

print(len(x))
