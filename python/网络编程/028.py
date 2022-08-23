# 客户端 TCP

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1",10101))#发起连接
