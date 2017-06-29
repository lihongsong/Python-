 # -*- coding:utf-8 -*-
from socket import *
from time import ctime

# 创建基于流的套接字
# socket(socket_family,socket_type,protocol=0)
# socket_family:[AF_UNIX,AF_INET] 基于文件和基于网络
# socket_type:[SOCKET_STREAM,SOCK_DGRAM] 基于流和基于数据报
# tcpSock = socket(AF_INET,SOCK_STREAM)

# 空的host表示可以使用任何可用的地址
HOST = ''
# 端口号
PORT = 21567
# 缓冲区大小
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSocket = socket(family = AF_INET,type = SOCK_STREAM)
# 套接字与地址绑定
tcpSocket.bind(ADDR)
# 监听连接 (ps:设置连接被转接或拒绝之前所能传入连接请求的最大值)
tcpSocket.listen(5)

while True:
    print("waiting for connection...")
    tcpCliSock,addr = tcpSocket.accept()
    print("...connected from:",addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(("[%s] %s" % (bytes(ctime(),"utf-8"),data)).encode("utf-8"))

    tcpCliSock.close()
tcpSocket.close()
