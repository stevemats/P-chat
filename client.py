#Python 3.7. 
import socket
import sys
import time

s=socket.socket()
host = input(str("Please enter the hostname of the server : "))
port = 8080
s.connect((host,port))
print("connected to chat server")
while 1:
            incoming_message = s.recv(1024)
            #now decoding the message after reaching the >> end user
            incoming_message = incoming_message.decode()
            print("Server : ",incoming_message)
            print("") 
            message = input(str(">>"))
            #and ow we convert mes to bytes
            #>> to showercase in terminal
            message = message.encode()
            s.send(message)
            print("message successfully sent..")
            print("")
