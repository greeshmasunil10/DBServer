# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:00:17 2020

@author: Greeshma
"""
import socket
import sys

HOST, PORT = "localhost", 9999
data = "greeshma"

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))