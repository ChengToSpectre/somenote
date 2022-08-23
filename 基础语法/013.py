#字符串的内置函数
'''
1. 大小写相关
capitalize() title() upper() lower() istitle()
str = 'slafjklsalf'

str.capitalize()字符串第一个字符大写
str.title() 字符串的所有单词首字母大写
str.upper() 所有字母大写
str.lower() 所有字母小写
str.istitle() 是否满足str.title这个形式?1:0

额外：
len(str) 求str的长度
{
 import random 
 a = random.randint(1,len(str))
}


2.查找
find() rfind() lfind() index() rindex() lindex() replace()
str = 'adsasjflasf'

str.find(s) 从0到结束查找s，找到返回str中的s的第一个坐标，否则返回-1
str.find(s,positon1,position2)  从position1到position2查找
str.rfind(s,position1,position2) 从右侧开始找
str.lfind(s,position1,position2) 从左侧开始找
str.index(s,......) 和find()差不多，如果没找到会报异常

3.编码，解码
encode decode
str='safasfgasg'
s1 = str.encode('UTF-8') 用UTF-8规则转换字符串
s2 = str.decode('UTF-8') 再将str转回来

4.内建函数
startswith() endswith() 都是返回bool数据
只能上次图片(jpg,png,bmp,gif)
filename = 'abab.doc'
result = filename.endswith('txt') 是否为txt结尾
startswith同理

5.
join(),
#gb2312 简体中文

'''