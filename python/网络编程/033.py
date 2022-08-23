#客户端

import os
import json
import socket
import struct

def send_data(conn,content):#给服务端发消息
    data = content.encode("utf-8")
    header = struct.pack("i",len(data))
    conn.sendall(header)
    conn.sendall(data)

def send_file(conn,file_path):
    file_size = os.stat(file_path).st_size#获取文件大小
    header = struct.pack('i',file_size)
    conn.sendall(header)

    has_send_size = 0
    file_object = open(file_path,mode='rb')
    while has_send_size<file_size:
        chunk = file_object.read(2048)
        conn.sendall(chunk)
        has_send_size += len(chunk)
    file_object.close()

def run():
    client = socket.socket()
    client.connect(("127.0.0.1",8001))

    while True:
         #"""
         #请求发送消息，格式为：
         #    -消息 ： msg|你好啊
         #    -文件 ： file|xxxx.png
         #"""
        content = input(">>>")

        if content.upper() == 'Q':
            send_data(client,"close")
            break

        input_text_list = conntent.split('|')
        if len(input_text_list)!=2:
            print("格式错误，请重试")
            continue

        massage_type, info = input_text_list
        #发消息
        if massage_type == 'msg':
            send_data(client, json.dumps({"msg_type":"msg"}))#发送消息类型

            send_data(client, info)#发送消息
        #发文件
        else:
            file_name = info.resplit(os.sep, maxsplit=1)[-1]

            send_data(client, json.dumps({"msg_type":"file","file_name":file_name}))#发送消息类型

            send_file(client, info)#发送消息

    client.close()

if __name__ == '__main__':
    run()