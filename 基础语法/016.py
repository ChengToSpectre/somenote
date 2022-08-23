#!/usr/bin/python3
 
#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
print ("------------------------")
printinfo( name="runoob" )
print ("------------------------")
printinfo("runoob")
print ("------------------------")
printinfo(35,"runoob")

print('*'*30)
#按顺序给函数传递

def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )#把这里把70挤出去 且只能多不能少

#只有list 和 dict可改变
#strings, tuples, 和 numbers 是不可更改的对象

def add(name,*args):
    print(args)#输出元组,可以为空
    sum = 0
    for i in range(len(args)):
        sum+=args[i]
    print(sum)

#add()
add(1,2)
add('dadada',1,2,3)

#可以参数只能放在不变参数的后面，有不变参数时传入的参数只能多不能少

# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

#可写函数说明
def printme( str,str1 ):
   "打印任何传入的字符串"
   print (str)
   return
 
#调用printme函数
printme( str1 = 'dadada',str = "菜鸟教程")


#def function() 一颗星*x自动生成元组，两星**x自动生成字典，传入key=value

#匿名函数
#lambda [arg1 [,arg2,.....argn]]:expression

x = lambda a : a + 10#只能写一行
print(x(5))