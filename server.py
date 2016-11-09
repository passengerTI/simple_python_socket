#!/usr/bin/python

from socket import socket

for i in range(10):
 s = socket()
 s.bind(('0.0.0.0',2222))
 s.listen(10)
 conn, addr = s.accept()
 print(i,'connected: ',addr)

 while True:
  data = conn.recv(1024)
  if (not data) or (data == 'close'):
   break
  conn.send(data.upper())
 conn.close()


