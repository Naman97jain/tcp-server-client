import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # Creation of socket object
print("Socket successfully created")
port = 3004

s.bind(('',port))
print(f"Socket binded to port:{port}")

s.listen(3)
print("Server is listening")
# p = "Thankyou for connecting"
while True:
    c, addr = s.accept()
    print(f"Got connection from {addr} and {c}")
    r = input("Enter message to be sent to client")
    r = r.encode()
    c.send(r)
    data = c.recvfrom(1024)
    print(data)
    c.close()