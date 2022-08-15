import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
cmd = "GET http://data.pr4e.org/romeo.txt ".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) > 1):
        break
    print(data.decode())
mysock.close()




#在terminal 訪問網站
    #telnet data.pr4e.org 80
    #GET http://data.pr4e.org/romeo.txt HTTP/1.0   >>>老師教的失敗
    #GET http://data.pr4e.org/romeo.txt   >>>>>>>>>>>>自己用的成功