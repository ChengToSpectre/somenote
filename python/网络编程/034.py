# io多路复用  
#服务器

import socket
import select

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setblocking(False)              # 加上变为非阻塞
s.bind(("127.0.0.1",8001))
s.listen(5)

inputs = [s,]#socket 对象列表
 
while True:
    #检测是否有客户端发起链接
    r,w,e = select.select(inputs, [], [],0.05)#每0.05秒检测一次
    for sock in r:
        if sock == s:
            conn,addr = sock.accept()
            print("有新链接")
            inputs.append(conn)
        else:
            data = sock.recv(1024)
            if data:
                print("收到消息:",data)
            else:
                print("关闭连接")
                inputs.remove(sock)