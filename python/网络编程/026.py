#客户端 UDP

import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    text = input("要发送的内容:")
    client.sendto(text.encode("utf-8"),("127.0.0.1",10100))
    data,(host,port) = client.recvfrom(1024)
    print(data,host,port)
    print(data.decode("utf-8"))
    break