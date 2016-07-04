import xmlrpclib
import sys
import time
import math
from threading import Thread
from datetime import datetime, timedelta
from random import randrange

N = 10 #10^8
vector = [0]*N

if len(sys.argv) != 4:
    print "Verify the functions parameters.\n"
    exit(1)
else:
	K = int(sys.argv[1])
	OP = int(sys.argv[2])  # 1 = Add; 2 = Pow; 3 = Mul
	X = int(sys.argv[3])


mdelay = timedelta(0)
tempo1 = datetime.now()

def divide_vector(n, k):
	n_p_threads = math.ceil(n/k)
	if (n%k != 0):
		n_p_threads += 1
	return int(n_p_threads)

def add_random_number(inicio, fim):
	for i in range(inicio, fim):
		vector[i] = randrange(0, 100)

def rpc_call(inicio, fim, x):
	server = xmlrpclib.ServerProxy('http://localhost:8000')
	if(OP == 1):
		for i in range(inicio, fim):
			vector[i] = server.add(vector[i], x)
	elif(OP == 2):
		for i in range(inicio, fim):
			vector[i] = server.pow(vector[i], x)
	elif(OP == 3):
		for i in range(inicio, fim):
			vector[i] = server.mul(vector[i], x)
	else:
		print "Operation not valid! Please select: 1 = Add; 2 = Pow; 3 = Mul."

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

for i in vector:
	print i

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

print "_______________"
for i in vector:
	print i

tempo2 = datetime.now()   
mdelay = mdelay + (tempo2 - tempo1)
print mdelay

