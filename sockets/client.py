"""
Leslie Wilson
April 18, 2018
client.py

Summary: This code creates a client-side socket that connects to a server.
It makes a call (the fortune function) and sends it to the server.
"""

# Import socket module
import socket
# import function module
from function import *

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# using fortune from the function module
call = fortune() 
# send a thank you message to the client.
s.send(call)

# receive data from the server
print s.recv(1024)


# close the connection
s.close()
