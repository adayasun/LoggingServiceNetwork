"""
	FILE			: LoggingServiceNetwork.py
	PROJECT			: SENG2040 - Assign-03 (A-04)
	PROGRAMMER		: Amy Dayasundara, Paul Smith
	FIRST VERSION	: 2020-03-17
	DESCRIPTION		:
		Service file for logging messages using TCP.
		Logging information will be store in a text file
"""
#import libraries
import socket
import sys
import logging

"""
	Logging basics/ Advanced:	https://www.youtube.com/watch?v=-ARI4Cz-awo&t=741s  
								https://www.youtube.com/watch?v=jxmzY9soFXg&t=1007s
	DEBUG:		Detailed information, typically of interest only when diagnosing problems
	INFO:		Confirmation that things are working as expected
	WARNING:	An indication that comething unexpected happened, or indicative of some problem on the near future
				(e.g. 'disk space low'). The software is still working as expected.
	ERROR:		Due to a more serious problem, the software has not been able to perform some function.
	CRITICAL:	A serious error, indicating that the program itself may be unable to continue rinning. 
"""

#Set up TCP Server https://pymotw.com/2/socket/tcp.html

#Socket
socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binding to port
serverAddress = ('localhost', 10000) #change hardcoded path to something else // use commandline to do that
print('starting up on %s port %s', serverAddress)
socketConnection.bind(serverAddress)

#Listen for connections
socketConnection.listen(1)

while True:
	#Wait for a connection
	print( 'waiting for a connection ... ')
	(connection, clientAddress) = socketConnection.accept()

	try:
		print( 'connection from %s', clientAddress)
		#Recieve data to be input into logfile
		while True:
			data = connection.recv(1024)
			print( 'received "%s"', data)
			if data:
				print('sending data back to the client')
				connection.sendall(data)
			else:
				print ('no more data from %s', clientAddress)
				break
	finally:
        # Clean up the connection
		connection.close()
