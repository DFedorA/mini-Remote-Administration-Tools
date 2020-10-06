from socket import *
import os
# HOST = '127.0.0.1'
HOST = '192.168.0.103'
# HOST = '192.168.63.1'
PORT = 3000
BUFSIZE = 1024
SOCKADDR = (HOST,PORT)
uCliSock = socket(AF_INET,SOCK_DGRAM)
def start():
    print(" Для вывода текущих процессов нажмите [1] \n Для создания процесса нажмите [2]: ")
    data = input('>')
    if data == "1":
        return data
    if data == "2":
        print(" Введите путь для запуска")
        data = input('>')
        return data
while True:
    data = start()
    data = data.encode('cp1251')
    if not data: break
    uCliSock.sendto(data,SOCKADDR)
    data,addr =  uCliSock.recvfrom(BUFSIZE)
    if not data:break
    print(str(data))
uCliSock.close()