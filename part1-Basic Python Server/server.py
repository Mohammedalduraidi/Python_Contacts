from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
#Start by importing myHandler Class from requestHandler.py file
from requestHandler import myHandler
#Every server needs to listen on a port with a unique number. The
#standard port for HTTP servers is port 8000,
Port = 8080

try:
	#This statement creates a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', Port), myHandler)
	print 'Started httpserver on port ' , Port
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()