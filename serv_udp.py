from socket import *
import psutil
import  os,subprocess
HOST = ''
PORT = 3000
BUFSIZE = 1024
SOCKADDR = (HOST,PORT)
uServSock = socket(AF_INET,SOCK_DGRAM)
uServSock.bind(SOCKADDR)
while True:
    print("waiting")
    data, addr = uServSock.recvfrom(BUFSIZE)
    loc_data= data.decode('cp1251')
    print('recived from ', addr , ' data: ', loc_data)
    if loc_data == "1":
        prosess_list = []
        for proc in psutil.process_iter():
            try:
                proc_name = proc.name()
                prosess_list.append(proc_name)
            except:
                break
        message = '; '.join(prosess_list)
    else:
        code = subprocess.call(loc_data)
        if code == 0:
            message = "Success!"
            print("Success!")
        else:
            message = "Error!"
            print("Error!")
    answer = 'anser to ' + addr[0] + ', echo:  '+ message
    answer = answer.encode('cp1251')
    uServSock.sendto(answer,addr)
uServSock.close()