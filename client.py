import socket

t = socket.socket()

port = 3004

t.connect(('127.0.0.1',port))
data = t.recvfrom(1024)[0]
print(data)
t.send(data)
# print(t.recv(1024))

t.close()