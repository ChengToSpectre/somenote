#服务端 UDP

import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#DGRAM为UDP协议
server.bind(("127.0.0.1",10100))

while True:
    data,(host,port) = server.recvfrom(1024)#阻塞，等待客户端发信息
    print(data,host,port)
    server.sendto("ok".encode("utf-8"),(host,port))
    break