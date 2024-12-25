
import socket
c = socket.socket()
c.connect(('localhost',6500))
#send client information to server
name=input("Enter your name:")
c.send(bytes(name,'utf-8'))
#receive info from server
print(c.recv(1024).decode())