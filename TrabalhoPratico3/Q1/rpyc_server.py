import rpyc
import math
from datetime import datetime
import copy
from cStringIO import StringIO 
from numpy.lib import format 


rpyc.core.protocol.DEFAULT_CONFIG['allow_pickle'] = True

def from_string(s): 
    f = StringIO(s) 
    arr = format.read_array(f) 
    return arr 

def to_string(arr): 
    f = StringIO() 
    format.write_array(f, arr) 
    s = f.getvalue() 
    return s 

class MyServer(rpyc.Service):

	def exposed_add(self, str_vec, x):
		my_str_vec = copy.deepcopy(str_vec)
		vector = from_string(my_str_vec)
		size = len(vector)
		blocksize = int(math.ceil(size/8))
		#print ("blocksize: " + str(blocksize) + "\n")
		for i in xrange(0, (blocksize*8), 8):
			#print("fazendo de " + str(i) + " a " + str(i+7))
			vector[i] += x
			vector[i+1] += x
			vector[i+2] += x
			vector[i+3] += x
			vector[i+4] += x
			vector[i+5] += x
			vector[i+6] += x
			vector[i+7] += x
		if((blocksize*8) != size):
			#print("Faltou de: " + str(blocksize*8) + " a " + str(size))
			for i in range((blocksize*8), size):
				vector[i] += x
		return to_string(vector)

	def exposed_pow(self, str_vec, x):
		my_str_vec = copy.deepcopy(str_vec)
		vector = from_string(my_str_vec)
		size = len(vector)
		blocksize = int(math.ceil(size/8))
		#print ("blocksize: " + str(blocksize) + "\n")
		for i in xrange(0, (blocksize*8), 8):
			#print("fazendo de " + str(i) + " a " + str(i+7))
			vector[i] = pow(vector[i], x)
			vector[i+1] = pow(vector[i+1], x)
			vector[i+2] = pow(vector[i+2], x)
			vector[i+3] = pow(vector[i+3], x)
			vector[i+4] = pow(vector[i+4], x)
			vector[i+5] = pow(vector[i+5], x)
			vector[i+6] = pow(vector[i+6], x)
			vector[i+7] = pow(vector[i+7], x)
		if((blocksize*8) != size):
			#print("Faltou de: " + str(blocksize*8) + " a " + str(size))
			for i in range((blocksize*8), size):
				vector[i] += x
		return to_string(vector)

	def exposed_mul(self, str_vec, x):
		my_str_vec = copy.deepcopy(str_vec)
		vector = from_string(my_str_vec)
		size = len(vector)
		blocksize = int(math.ceil(size/8))
		#print ("blocksize: " + str(blocksize) + "\n")
		for i in xrange(0, (blocksize*8), 8):
			#print("fazendo de " + str(i) + " a " + str(i+7))
			vector[i] = vector[i] * x
			vector[i+1] = vector[i+1] * x
			vector[i+2] = vector[i+2] * x
			vector[i+3] = vector[i+3] * x
			vector[i+4] = vector[i+4] * x
			vector[i+5] = vector[i+5] * x
			vector[i+6] = vector[i+6] * x
			vector[i+7] = vector[i+7] * x
		if((blocksize*8) != size):
			#print("Faltou de: " + str(blocksize*8) + " a " + str(size))
			for i in range((blocksize*8), size):
				vector[i] += x
		return to_string(vector)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyServer, port = 18862)
    t.start()