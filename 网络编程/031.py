#粘包问题 客户端

import socket
import struct

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
jud = client.connect_ex(("127.0.0.1",10100))
if jud == 0:
    print("发送成功！")
else:
    print("发送失败！")

data = "dadadada".encode("utf-8")
header1 = struct.pack('i',len(data))
client.sendall(header1)
client.sendall(data)

data = "is klee".encode("utf-8")
header2 = struct.pack('i',len(data))
client.sendall(header2)
client.sendall(data)

client.close()