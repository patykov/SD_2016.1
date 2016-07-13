import rpyc
from datetime import datetime

class MyServer(rpyc.Service):

	def exposed_add(self, vector, x):
		for i in range(len(vector)):
			vector[i] += x
		return vector

	def exposed_pow(self, vector, x):
	    for i in range(len(vector)):
	    	vector[i] = pow(vector[i], x)
	    return vector

	def exposed_mul(self, vector, x):
	    for i in range(len(vector)):
	    	vector[i] = vector[i] * x
	    return vector


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyServer, port = 18861)
    t.start()