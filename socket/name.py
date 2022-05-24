import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="192.168.43.168"
port=9955
s.bind(( ip,port ))
data=[]

def get_data():
    a=input("how much os you want to  connect")
    a=int(a)

    for i in range(a):
        client_ip=input("Enter ip here")
        client_port=input("enter port here")
        client_port=int(client_port)
        record=[client_ip,client_port]
        data.append(record)
        
        
def connect():
    for i in data:
        # Type a message
        x = input("")
        # Give a OS IP in string  and PORT in digit numbers
        # Example s.sendto( "message".encode(), ( "IP", PORT_Number )
        # message should be encoded(message should be BYTE TYPE) due to network can only recieve byte type
        s.sendto("{}".format(x).encode(), (i[0],ip[1]))
        




get_data()

connect()

"""
    y=1
    while y==1:
        
        client_ip=app[0][1]
        port=9822
        data=app[0].decode()
        print(data)
        a=input("send some thing :")
        b = bytes(a, 'utf-8')
        client_ip.sendto(b,(client_ip,port))
"""
