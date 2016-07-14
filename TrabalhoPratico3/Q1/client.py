from datetime import datetime, timedelta
from cStringIO import StringIO 
from numpy.lib import format 
from threading import Thread
import numpy as np
import rpyc
import sys

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

def divide_vector(n, k):
	sizes = []
	splitsize = (1.0/k*n)
	for i in range(k):
		sizes.append([int(round(i*splitsize)), int(round((i+1)*splitsize))])
	return sizes

def rpc_call(inicio, fim, x):
	string_vec = to_string(vector[inicio:fim])
	if(OP == 1):
		vector[inicio:fim] = from_string( server.root.exposed_add(string_vec, x) )
	elif(OP == 2):
		vector[inicio:fim] = from_string( server.root.exposed_pow(string_vec, x) )
	elif(OP == 3):
		vector[inicio:fim] = from_string( server.root.exposed_mul(string_vec, x) )
	else:
		print "Operation not valid! Please select: 1 = Add; 2 = Pow; 3 = Mul."

def save_file(time):
	with open("/Users/admin/Documents/UFRJ/SD/SD_2016.1/TrabalhoPratico3/Q1/log.txt", "a") as file:
		file.write("Numero de threads: " + str(K) + " Operacao: " + str(OP) + " Tempo: " + str(time) + "\n")


N = 10000000 #10^7
vector = np.random.randint(100, size=N) #Initialize vector with random numbers
server = rpyc.connect("localhost", 18862)

if (len(sys.argv) != 4):
	print "Verify the functions parameters.\n"
  	exit(1)
else:
	K = int(sys.argv[1])   #number of threads
	OP = int(sys.argv[2])  # 1 = Add; 2 = Pow; 3 = Mul
	X = int(sys.argv[3])   #int parameter to the functions


if __name__ == "__main__":
	sizes = divide_vector(N, K)
	threads = []
	i = 0

	#Calculating time
	mdelay = timedelta(0)
	tempo1 = datetime.now()

	#Call rpc function for each thread
	for k in range(K):
		size = sizes[k]
		t = Thread(target=rpc_call, args=(size[0], size[1], X))
		t.start()
		threads.append(t)	 
	for t in threads:
		t.join()

	tempo2 = datetime.now()
	mdelay = (tempo2 - tempo1)
	save_file(mdelay)
	exit(0)

