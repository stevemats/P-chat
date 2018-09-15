#Python 3.7.0a4 (v3.7.0a4:07c9d85, Jan  9 2018, 07:07:02) [MSC v.1900 64 bit (AMD64)] on win32
#Type "copyright", "credits" or "license()" for more information.
#stevemats
#>>> 
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
