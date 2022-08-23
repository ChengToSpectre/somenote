#粘包实例 服务端

import struct
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",10100))
server.listen(10)

conn,addr = server.accept()
print(conn)
print(addr)

header = conn.recv(4)
data_lenght1 = struct.unpack('i', header)[0]
print("长度为:",data_lenght1)
has_recv_len = 0
data1=""
while True:
    length = data_lenght1
    if length>1024:
        length = 1024
    else:
        length = data_lenght1

    datat = conn.recv(length).decode("utf-8")#存在一次收不完的情况，可以计算长度再次收取，直到全部数据收完
    data1 += datat
    has_recv_len = len(data1)

    if has_recv_len == data_lenght1:
        break
print("数据为",data1)

header = conn.recv(4)
data_lenght2 = struct.unpack('i', header)[0]
print("长度为:",data_lenght2)
has_recv_len = 0
data2=""
while True:
    length = data_lenght2
    if length>1024:
        length = 1024
    else:
        length = data_lenght2

    datat = conn.recv(length).decode("utf-8")
    data2 += datat
    has_recv_len = len(data2)

    if has_recv_len == data_lenght2:
        break
print("数据为",data2)

conn.close()
server.close()

