from SimpleXMLRPCServer import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 8000))

queue = []

def receive_msg(msg, myTime, myId):
	while(1):
		if (len(queue) > 0):
			if(myId == queue[0]):
				return GRANT

		#REQUEST
		if (msg == 1):
			if(len(queue) == 0):
				return GRANT
			queue.append(myId)

		#RELEASE
		elif(msg == 2):
			remove a posicao 0 da lista e empurra geral uma posicao pra frente
			return BELEZINHA
			
		else
			print "Error"
			exit(1)

    
server.register_function(receive_msg, 'send_msg')



try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
	
    print 'Exiting'