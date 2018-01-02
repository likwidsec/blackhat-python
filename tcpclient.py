#!/usr/bin/env python
##########################
# quick dirty tcp client #
#    -likwid 1/18-	 #
##########################

import socket, sys

host = "127.0.0.1"
port = 31337

#create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((host, port))

#send some data ...
cdata = sys.argv[1]
client.send("%s\r\n\r\n" % (cdata))

print "[*] Sent: %s" % (cdata)
#receive some data ... 4096 bytes to be exact
response = client.recv(4096)
print response
