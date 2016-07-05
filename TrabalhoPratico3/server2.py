from SimpleXMLRPCServer import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 8000))

queue = []

def receive_msg(msg, myTime, myId):
	#REQUEST
	if (msg == 1):
		if(len(queue) == 0):
			ENVIA GRANT
		queue.append(myTime)

	#RELEASE
	elif(msg == 2):
		queue.remove(myTime)
		if (len(queue) > 0):
			ENVIA GRANT PARA queue[0].

	else
		print "Error"
		exit(1)
    
    return 
server.register_function(receive_msg, 'send_msg')



try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
	
    print 'Exiting'