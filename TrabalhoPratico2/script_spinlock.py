from subprocess import call
import datetime
from datetime import datetime, timedelta
import threading
from threading import Thread

mdelay = timedelta(0)
#num_thread = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30]
num_thread = [7]
num_vector = [9]

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
			tempo2 = datetime.now()      
	
			mdelay = mdelay + (tempo2 - tempo1)

		print "Numero de threads: " + str(k) + " Tamanho do vetor: 10^" + str(N) + " Tempo medio total: " + str(mdelay/10) + "\n\n"


