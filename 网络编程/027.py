# 服务端 tcp

import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#流协议即tcp

server.bind(("127.0.0.1",10101))

server.listen(5)

while True:
    conn,addr = server.accept()  #等待客户连接