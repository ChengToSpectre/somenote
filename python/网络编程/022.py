import socket

#向指定IP发起连接请求
client = socket.socket()
client.connect(("192.168.0.23",8080))# 向服务端发起连接（阻塞）

#连接成功后，发送消息
client.send("hello".encode("UTF-8"))

#等待服务端消息回复
reply = client.recv(1024)
print(reply.decode("UTF-8"))

#关闭连接
client.close()