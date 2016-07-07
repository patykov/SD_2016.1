import xmlrpclib
import sys
import math
from threading import Thread
from datetime import datetime, timedelta
from random import randrange

N = 100000000 #10^8
vector = [0]*N
server = xmlrpclib.ServerProxy('http://localhost:8000')

if (len(sys.argv) != 4):
	print "Verify the functions parameters.\n"
  	exit(1)
else:
	K = int(sys.argv[1])
	OP = int(sys.argv[2])  # 1 = Add; 2 = Pow; 3 = Mul
	X = int(sys.argv[3])

def divide_vector(n, k):
	n_p_threads = math.ceil(n/k)
	if (n%k != 0):
		n_p_threads += 1
	return int(n_p_threads)

def add_random_number(inicio, fim):
	for i in range(inicio, fim):
		vector[i] = randrange(0, 100)

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
	with open("/Users/admin/Documents/UFRJ/SD/SD_2016.1/TrabalhoPratico3/log.txt", "a") as file:
		file.write(str(time) + "\n")


if __name__ == "__main__":
	number_per_threads = divide_vector(N, K)
	i = 0
	threads = []
	#Populate the vector with random numbers
	while(i<N):
		f = i + number_per_threads
		if(f>=N):
			f = N
		t = Thread(target=add_random_number, args=(i, f))
		t.start()
		i += number_per_threads
		threads.append(t)
	for t in threads:
		t.join()
	del threads[:]

	#Calculating time
	mdelay = timedelta(0)
	tempo1 = datetime.now()

	i = 0
	#Call rpc function for each thread
	while(i<N):
		f = i + number_per_threads
		if(f>=N):
			f = N
		t = Thread(target=rpc_call, args=(i, f, X))
		t.start()
		i += number_per_threads
		threads.append(t)
	for t in threads:
		t.join()


	tempo2 = datetime.now()   
	mdelay = mdelay + (tempo2 - tempo1)
	save_file(mdelay)


