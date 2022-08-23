# name = "sb"

# n = int(input("请输入数量"))

# for i in range(n):
#     print("{}正在吃第{}个".format(name,i+1))

# i=0
# while i<10:
#     i = i+1
#     print(i)

# i = 1
# ans = 1
# while i<=30 :
#     ans = ans*i
#     i = i+1
# print(ans)

i = 1
while i<=4 :
    j = 1
    while j <= 9:
        if j> 9/2+1-i and j<9-(9/2-i) :print("{}".format(i),end="")
        else : print(" ")
        j = j+1
    i = i+2
    print("")
