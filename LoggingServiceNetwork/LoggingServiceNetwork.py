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
import json
from config import *

#For testing purpose
import math

#loggingInfo = { }

"""
	Logging basics/ Advanced:	https://www.youtube.com/watch?v=-ARI4Cz-awo&t=741s  
								https://www.youtube.com/watch?v=jxmzY9soFXg&t=1007s

	0  NOTSET
	10 DEBUG:		Detailed information, typically of interest only when diagnosing problems
	20 INFO:		Confirmation that things are working as expected
	30 WARNING:		An indication that comething unexpected happened, or indicative of some problem on the near future
					(e.g. 'disk space low'). The software is still working as expected.
	40 ERROR:		Due to a more serious problem, the software has not been able to perform some function.
	50 CRITICAL:	A serious error, indicating that the program itself may be unable to continue rinning. 
"""

###Play with logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

LOG_FORMAT = logging.Formatter('%(levelname)s %(asctime)s : %(message)s')

#adding a file handler to the logger
file_handler = logging.FileHandler('..\\..\\Newtest.Log')
file_handler.setFormatter(LOG_FORMAT)
logger.addHandler(file_handler)

def quadratic_formula(a,b,c):
		###Return the solutions to the equation ax^2 + bx + c = 0
		logger.info("Quadratic_formula({0},{1},{2})".format(a, b, c))

		#Compute the discriminant
		disc = b^2 - 4*a*c

		logger.debug("Compute the two roots")
		root1 = (-b + math.sqrt(disc)) / (2*a)
		root2 = (-b - math.sqrt(disc)) / (2*a)
	
		#Return the roots
		logger.debug("# Return the roots")
		return (root1, root2)

roots = quadratic_formula(1,0,-4)
print(roots)

#PARSE INFO INTO LOGGER 
#NEED TO KNOW WHICH ONE TO USE TO LOG LEVEL
def parseLogInfo(logInfo):
	levelType = logInfo.get("level")
	levelMsg = logInfo.get("message")
	if levelType == "DEBUG":
		logger.debug(levelMsg)
	elif levelType == "INFO":
		print(levelType)
		logger.info(levelMsg)
	elif levelType == "WARNING":
		print(levelType)
		logger.warning(levelMsg)
	elif levelType == "ERROR":
		print(levelType)
		logger.error(levelMsg)
	elif levelType == "CRITICAL":
		print(levelType)
		logger.critical(levelMsg)

###Set up TCP Server https://pymotw.com/2/socket/tcp.html####

#Socket
socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketConnection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Overcome address already in use
#Binding to port
serverAddress = (IP, PORT) #change hardcoded path to something else // use commandline to do that
print('starting up on %s port %s', serverAddress)
socketConnection.bind(serverAddress)

#Listen for connections
socketConnection.listen(1)

#Create list to keep track of clients
socketList = {serverAddress}
clients = {}

while True:

	#Wait for a connection
	print( 'waiting for a connection ... ')
	(connection, clientAddress) = socketConnection.accept()

	try:
		print( 'connection from %s', clientAddress)
		
		while True:
			data = connection.recv(1024)
			#check if it is a new or existing connection based 
			#off file handler list? -- CREATE THREAD to run 
			#multiple clients

			print( 'received: ', data)
			if data:
				#Recieve data to be input into logfile
				print('sending data back to the client')
				connection.sendall(data)
				loggingInfo = json.loads(data.decode('utf-8').strip())
				parseLogInfo(loggingInfo)
			else:
				print ('no more data from', clientAddress)
				break
	finally:
        # Clean up the connection
		connection.close()
