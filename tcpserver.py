#!/usr/bin/env python
###########################
#    simple tcp server    #
#      -likwid 1/18-	  #
###########################

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

#create our socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#set our server details - IP and port to listen on.
server.bind((bind_ip, bind_port))

#specify the amount of max connections to allow
server.listen(5)


print "[*] Listening on %s:%d" % (bind_ip, bind_port)

#this is our client handling thread
def handle_client(client_socket):

	#print out what the client sends when they connect
	request = client_socket.recv(1024)
	print "[*] Received: %s" % request

	#send back something to the connecting client..
	client_socket.send("ACK!")

	#make sure to close our socket when we're finished with it
	client_socket.close()


while True:

	client, addr = server.accept()

	print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

	#spin up our client thread to handle incoming data
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start()
