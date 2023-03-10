"""
REMOTE ACCESS v 0.1
By: cveExplorer
"""

import socket as sock
import sys
import os

s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
s.bind(("127.0.0.1", 9090))
s.listen(1)

while True:
	conn,addr = s.accept()
	print("New connection from", addr)
	data = s.recv(1024)
	print("Data received\n")
	print(str(data.decode('utf-8')))
	print("Closing connection to", addr)
	conn.close()
	print("Closing socket...")
	s.close()
	break

sys.exit(0)
