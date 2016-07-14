from SimpleXMLRPCServer import SimpleXMLRPCServer


server = SimpleXMLRPCServer(("localhost", 8000))


def adder_function(vector, x):
    for i in range(len(vector)):
    	vector[i] += x
    return vector
server.register_function(adder_function, 'add')

def pow_function(vector, x):
    for i in range(len(vector)):
    	vector[i] = pow(vector[i], x)
    return vector
server.register_function(pow_function, 'mypow')

def mul_function(vector, x):
    for i in range(len(vector)):
    	vector[i] = vector[i] * x
    return vector
server.register_function(mul_function, 'mul')


try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
	
    print 'Exiting'