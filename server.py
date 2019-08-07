import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # Creation of socket object
print("Socket successfully created")
port = 3004

s.bind(('',port))
print(f"Socket binded to port:{port}")

s.listen(3)
print("Server is listening")
p = "Thankyou for connecting"
while True:
    c, addr = s.accept()
    print(f"Got connection from {addr} and {c}")
    r = p.encode()
    c.send(r)
    c.close()