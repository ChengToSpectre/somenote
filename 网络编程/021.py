# 套接字sockets
import socket

#创建服务端

#def server():

print("sever beign!!!\n")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#流式Socket
#s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#数据报告式
s.bind(('192.168.0.23',8080))                           #绑定地址
s.listen(3)                                         #最多3个链接
while True:
    conn,addr = s.accept()
    print("welcome{}".format(addr))
    data=conn.recv(1024)
    dt=data.decode('UTF-8')                     #接受一个1024字节的数据
    print("Receive:",dt)
    # aa=input('服务器发送：')
    # if aa =='quit':
    #     conn.close()
    #     s.close()
    # else:
    #     conn.send(aa.encode('utf-8'))           #发送数据
    conn.sendall("Hello World!".encode("UTF-8"))
    conn.close()
s.close()

