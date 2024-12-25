import socket

s = socket.socket()
print('Socket Created')
s.bind(('localhost', 6500))
s.listen(3)
print('waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("connected with", addr, name)

    c.send(bytes('Welcome to Bangladesh server', 'utf-8'))
