#!/usr/bin/env python
import socket

s=socket.socket()
host=socket.gethostname()
print("server will start on host:",host)
port=8080
# make sure the port is not in use
s.bind((host,port))
print("")
print("server done binding on host and port successfully")
print("")
print("server is waiting for incoming connections")
print("")
s.listen(1)
conn,addr = s.accept()
print(addr,"Has connected to the server and is now online...")
print("")
#putting in a loop
while 1:
            message = input(str(">>"))
            # Now converting our message to bytes
            message = message.encode()
            conn.send(message)
            print("message successfully sent..")
            print("")
            incoming_message = conn.recv(1024)
            # decoding the bytes into readable output
            incoming_message = incoming_message.decode()
            print("client : ",incoming_message)
            print("") 
