from subprocess import call
import datetime
from datetime import datetime, timedelta
import threading
from threading import Thread

mdelay = timedelta(0)
#num_thread = [[1, 1], [2, 2], [5, 5], [10, 10], [2, 10], [10, 2]]
num_thread = [[10, 10], [2, 10]]
num_vector = [2, 4, 8, 16, 32]

#For "producer_consumer.c"
def func1():
	cmd = "./produtor_consumidor 2 1 1"
	call(cmd, shell = True)
for x in xrange(1,10):
	tempo1 = datetime.now()
	Thread = threading.Thread(target = func1)	
	Thread.start()
	tempo2 = datetime.now()      
	
	mdelay = mdelay + (tempo2 - tempo1)

print " Tempo medio total: " + str(mdelay/10) + "\n\n"

