  
# importing libraries
import socket as skt
import threading as thd
import os
import time

# design
print()
os.system(" tput setaf 1 ")
print("\t-----------------------------------------------")
os.system(" tput setaf 7 ")
print(" \t\t>>>>Welcome in this Chit-Chat App<<<< ")
os.system(" tput setaf 35 ")
print("\t-----------------------------------------------\n")
os.system(" tput setaf 23 ")

# ip address
os.system(" tput setaf 5 ")
remote_ip = input("Enter your partner's ip address : ")
local_ip = "192.168.43.67"
print()

# bind local ip
s = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
port = 1234
s.bind(( local_ip, port ))

# function to receive the msg
def msgrecv():
	while True:
		x = s.recvfrom(1024)
		client_ip = x[1][0]
		client_data = x[0].decode()

		if client_data == "quit":
			os._exit(1)
		print( client_ip + "(harry)" + "  :   " + client_data )

# function to send the msg
def msgsend():
	while True:
		send_msg = input()
		s.sendto( send_msg.encode(), ( remote_ip, port ))
		if send_msg == "quit":
			os._exit(1)

# creating thread to send the message
send_thd = thd.Thread(target=msgsend)

# creating thread to receive the message
recv_thd = thd.Thread(target=msgrecv)

# starting threads
recv_thd.start()

send_thd.start()
