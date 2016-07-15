from datetime import datetime
from cStringIO import StringIO 
from numpy.lib import format
import copy
import rpyc
import math

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
		vector = from_string(str_vec)
		size = len(vector)
		blocksize = int(math.ceil(size/8))
		for i in xrange(0, (blocksize*8), 8):
			vector[i] += x
			vector[i+1] += x
			vector[i+2] += x
			vector[i+3] += x
			vector[i+4] += x
			vector[i+5] += x
			vector[i+6] += x
			vector[i+7] += x
		if((blocksize*8) != size):
			for i in range((blocksize*8), size):
				vector[i] += x
		return to_string(vector)

	def exposed_pow(self, str_vec, x):
		vector = from_string(str_vec)
		size = len(vector)
		blocksize = int(math.ceil(size/8))
		for i in xrange(0, (blocksize*8), 8):
			vector[i] = pow(vector[i], x)
			vector[i+1] = pow(vector[i+1], x)
			vector[i+2] = pow(vector[i+2], x)
			vector[i+3] = pow(vector[i+3], x)
			vector[i+4] = pow(vector[i+4], x)
			vector[i+5] = pow(vector[i+5], x)
			vector[i+6] = pow(vector[i+6], x)
			vector[i+7] = pow(vector[i+7], x)
		if((blocksize*8) != size):
			for i in range((blocksize*8), size):
				vector[i] += x
		return to_string(vector)

	def exposed_mul(self, str_vec, x):
		vector = from_string(str_vec)
		size = len(vector)
		blocksize = int(math.ceil(size/8))
		for i in xrange(0, (blocksize*8), 8):
			vector[i] = vector[i] * x
			vector[i+1] = vector[i+1] * x
			vector[i+2] = vector[i+2] * x
			vector[i+3] = vector[i+3] * x
			vector[i+4] = vector[i+4] * x
			vector[i+5] = vector[i+5] * x
			vector[i+6] = vector[i+6] * x
			vector[i+7] = vector[i+7] * x
		if((blocksize*8) != size):
			for i in range((blocksize*8), size):
				vector[i] += x
		return to_string(vector)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyServer, port = 18862)
    t.start()