#!/usr/bin/env python
##############################
# quick and dirty udp client #
#       -likwid 1/18-	     #
##############################

import socket

host = "127.0.0.1"
port = 80

#create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data...
client.sendto("AAAABBBBCCCC", (host, port))

#receive some data...
data, addr = client.recvfrom(4096)

print data

