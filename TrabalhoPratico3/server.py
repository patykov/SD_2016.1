from SimpleXMLRPCServer import SimpleXMLRPCServer


server = SimpleXMLRPCServer(("localhost", 8000))

server.register_function(pow)

def adder_function(x,y):
    return x + y
server.register_function(adder_function, 'add')

def mul_function(x, y):
        return x * y
server.register_function(mul_function, 'mul')


try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
	
    print 'Exiting'