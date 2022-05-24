import socket 
import threading 

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

ip="192.168.43.168"
port=9826
msg=s.bind(( ip,port ))
s.listen()
csession,addr=s.accept()

y=1
while y==1:
    app=csession.recv(100)
    print(app)
    a=input("send some thing :")
    b = bytes(a, 'utf-8')
    csession.send(b)
    
"""
y=1

def lwchat():
    while y==1:
        app=csession.recv(100)
        a=input("send some thing :")
        b = bytes(a, 'utf-8')
        csession.send(b)
        return app
lwchat()
"""
