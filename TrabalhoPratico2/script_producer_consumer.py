from subprocess import call
import datetime
from datetime import datetime, timedelta
import threading
from threading import Thread

mdelay = timedelta(0)
num_thread = [[1, 1], [2, 2], [5, 5], [10, 10], [2, 10], [10, 2]]
num_vector = [2, 4, 8, 16, 32]

#For "producer_consumer.c"
for k in num_thread:
	for N in num_vector:
		def func1():
			cmd = "./produtor_consumidor " + str(N) + " " + str(k[0]) + " " + str(k[1])
			call(cmd, shell = True)
		for x in xrange(1,10):
			tempo1 = datetime.now()
			Thread = threading.Thread(target = func1)	
			Thread.start()
			Thread.join()
			tempo2 = datetime.now()      
	
			mdelay = mdelay + (tempo2 - tempo1)

		print "Numero de threads: " + str(k) + " Tamanho do vetor: " + str(N) + " Tempo medio total: " + str(mdelay/10) + "\n\n"
		mdelay = timedelta(0)


