import xmlrpclib
import sys
import math
from threading import Thread
from datetime import datetime, timedelta
import numpy.random as nprnd


def divide_vector(n, k):
	sizes = []
	splitsize = (1.0/k*n)
	for i in range(k):
		sizes.append([int(round(i*splitsize)), int(round((i+1)*splitsize))])
	return sizes

def rpc_call(inicio, fim, x):
	if(OP == 1):
		vector[inicio:fim] = server.add(vector[inicio:fim], x)
	elif(OP == 2):
		vector[inicio:fim] = server.mypow(vector[inicio:fim], x)
	elif(OP == 3):
		vector[inicio:fim] = server.mul(vector[inicio:fim], x)
	else:
		print "Operation not valid! Please select: 1 = Add; 2 = Pow; 3 = Mul."

def save_file(time):
	with open("/Users/admin/Documents/UFRJ/SD/SD_2016.1/TrabalhoPratico3/Q1/log.txt", "a") as file:
		file.write(str(time) + "\n")


N = 100000000 #10^8
np_vector = nprnd.randint(100, size=N) #Initialize vector with random numbers
vector = np_vector.tolist()            #Transform the numpy array into a simple python list
server = xmlrpclib.ServerProxy('http://localhost:8000')

if (len(sys.argv) != 4):
	print "Verify the functions parameters.\n"
  	exit(1)
else:
	K = int(sys.argv[1])   #number of threads
	OP = int(sys.argv[2])  # 1 = Add; 2 = Pow; 3 = Mul
	X = int(sys.argv[3])   #int parameter to the functions


if __name__ == "__main__":
	#number_per_threads = divide_vector(N, K)
	sizes = divide_vector(N, K)
	threads = []

	#Calculating time
	mdelay = timedelta(0)
	tempo1 = datetime.now()

	i = 0
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


