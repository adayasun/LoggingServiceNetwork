"""
	FILE			: LoggingServiceNetwork.py
	PROJECT			: SENG2040 - Assign-03 (A-04)
	PROGRAMMER		: Amy Dayasundara
	FIRST VERSION	: 2020-03-17
	DESCRIPTION		:
		Service file for logging messages using TCP.
		Logging information will be store in a text file
"""
#import libraries
import socket
import sys


#Set up TCP Server https://pymotw.com/2/socket/tcp.html

#Socket
socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding to port
serverAddress = ('localhost', 10000) #change hardcoded path to something else // use commandline to do that
print >>sys.stderr, 'starting up on %s port %s' % server_address
socketConnection.bind(server_address)

#Listen for connections
socketConnection.listen(1)

while True:
	#Wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	connection = socketConnection.accept()
	clientAddress = socketConnection.accept()

	try:
		print>>sys.stderr, 'connection from', clientAddress
		#Recieve data to be input into logfile
		while True:
			data = connection.recv(16)
			print >>sys.stderr, 'received "%s"' % data
			if data:
				print >>sys.stderr, 'sending data back to the client'
				connection.sendall(data)
			else:
				print >>sys.stderr, 'no more data from', client_address
				break
	finally:
        # Clean up the connection
		connection.close()
