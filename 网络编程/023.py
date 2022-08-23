import socket

s = socket.socket()
s.bind(("192.168.0.2",10100))
s.listen(100)

while True:
    conn,addr = s.accept()
    userword = conn.recv(1024).decode("UTF-8")
    password = conn.recv(1024).decode("UTF-8")
    if(userword == 'admin' and password == '123456'):
        print("连接成功!")
        conn.send("yes".encode("UTF-8"))
    else:
        print("连接失败!")
        conn.send("no".encode("UTF-8"))
