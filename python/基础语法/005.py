a = int(input("第一个数字："))
b = int(input("第二个数字："))

def cal(a,b):
    return a if b == 0 else cal(b,a%b)

def swap(a,b):
    if(a>b):
        t = a
        a = b
        b = t
    return a,b

if (a<b):
    swap(a,b)

print(a,b)

print(cal(a,b))