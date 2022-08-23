#!/usr/bin/env python
#-*- coding:utf-8 -*-

import socket
import select

ip_port = ("192.168.12.172", 9999)
sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk1.bind(ip_port)
sk1.listen(5)
sk1.setblocking(0)

inputs = [sk1,]

print "inputs: ", inputs
while True:
    #要不断的调用select函数来检查给定的类文件对象是否有数据就绪，当且仅当有新客户端连接进来的时候，sk1服务端这个套接字对象才是读就绪的，也就是才会存在于readable_list列表中；
    readable_list, writeable_list, error_list = select.select(inputs, [], inputs, 1)
    print "readable_list: ", readable_list
    for r in readable_list:
        #当客户端第一次连接服务端时，sk1服务端套接字对象，通过调用accept方法获取到新进来的客户端套接字，然后把新进来的客户端套接字对象追加到，待select检测的inputs列表中。
        if sk1 == r:
            print "r=sk1: ", r
            print "first accept"
            request, address = r.accept()
            request.setblocking(0)
            inputs.append(request)
            print "first inputs: ", inputs
        #当客户端连接上服务器端之后，再次发送数据时
        else:
            print "myr: ", r
            received = r.recv(1024)
            print "received: ", received
            #当正常接收客户端发送的数据时
            if received:
                print "received data: ", received
            #当客户端关闭程序时
            else:
                inputs.remove(r)
sk1.close()
