from SimpleXMLRPCServer import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("localhost", 8000))

queue = []

def receive_request(myTime, myId):
	queue.append(myId)
	print("add na fila" + str(myId))
	while True:
		if((len(queue) == 0) or (queue[0] == myId)):
			print("enviei o GRANT" + str(myId))
			return 1 #GRANT

server.register_function(receive_request, 'ask_request')


def receive_release(myTime, myId):
	print("removi da fila" + str(myId))
	del queue[0]
	print queue
	return 1 #SLEEP
		    
server.register_function(receive_release, 'send_release')

def aff():
	print("uhuuul")
server.register_function(aff, 'printando')


try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
	
    print 'Exiting'