from subprocess import call
import datetime
from datetime import datetime, timedelta
import threading
from threading import Thread

mdelay = timedelta(0)
num_thread = [30]
num_vector = [10]

print "Spinlock\n"
#For "spinlock.c"
for k in num_thread:
	for N in num_vector:
		def func1():
			cmd = "./spinlock " + str(k) + " " + str(N)
			call(cmd, shell = True)
		for x in xrange(1,10):
			tempo1 = datetime.now()
			Thread = threading.Thread(target = func1)
			Thread.start()
			Thread.join()
			tempo2 = datetime.now()      
	
			mdelay = mdelay + (tempo2 - tempo1)

		print "Numero de threads: " + str(k) + " Tamanho do vetor: 10^" + str(N) + " Tempo medio total: " + str(mdelay/10) + "\n\n"
		mdelay = timedelta(0)


#Numero de threads: 15 Tamanho do vetor: 10^10 Tempo medio total: 0:00:39.768043
#Numero de threads: 20 Tamanho do vetor: 10^10 Tempo medio total: 0:00:38.992455