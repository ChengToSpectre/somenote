

print("aaa",end="")
print("nnn")
print("ccc",end="")
print("ddd")

# 转义字符 \n(换行)  \t \'(单引号)  \"(双引号)  \r(回车) \\
#print("sbxxx:\n,\t请点击连接")

a = "str"
a += "ing"

print(id(a),a)
#string 加减，id为地址

b = a
print(id(b),id(a),b)
# '='为地址的赋值

a = int(input("第一个数字："))
b = int(input("第二个数字："))



result = a>b  # 自动为bool型参数

print(result)