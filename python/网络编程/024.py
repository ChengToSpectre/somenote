import socket

s = socket.socket()
s.connect(("192.168.0.2",10100))

while True:
    userword = input("请输入用户名:")
    password = input("请输入密码:")
    if userword == 'q' or userword == 'Q' or password =='q' or password == 'Q':
        break
    s.sendall(userword.encode("UTF-8"))
    s.sendall(password.encode("UTF-8"))

    jud1 = s.recv(1024).decode("UTF-8")

    if jud1 == "yes":
        print("登录成功!")
    else:
        print("登录失败")