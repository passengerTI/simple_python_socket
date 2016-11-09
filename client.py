#!/usr/bin/python

from socket import socket

s = socket()
s.connect(('localhost',2222))
s.send('hello!')

data = s.recv(1024)
s.close

print(data)