s='781234569'

list1=[]
for i in range(len(s)):
    list1.append(s[i])

print(list1)
s1 = set()#只能这样创建空集合
s2 = {1,3,7}#无: 则生成集合非字典
#set会自动去重,但是顺序随机

s3 = set(list1)
s3.add('10')
s3.add('11')
print(s3)

#add(e)添加元素e，update(e)添加e中的多个元素，例:s3.update(t) t=(101,102,103) 添加101，102，103三个元素
#remove()  pop()  discard(e)(删除指定e元素)
#union() 返回并集 集合不可加，但可减，减位差集 可以用&，得到交集 |得到并集
print('-'*30)
thisset = set({"Google", "Runoob", "Taobao"})
len(thisset)
print(len(thisset))

print('*'*30)
set1 = {1,3,5,7,9}
set2 = {2,4,5,8}
set3 = {1}
set3.update(set1)
print(set3)
print(set1-set2)

set1.update(set2)
print(set1)

set3 = set3.union(set2)
print(set3)