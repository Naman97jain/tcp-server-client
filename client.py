import socket

t = socket.socket()

port = 3004

t.connect(('127.0.0.1',port))
print(t.recv(1024))

t.close()