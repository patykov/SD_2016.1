from subprocess import call
import datetime
from datetime import datetime, timedelta
import threading
from threading import Thread

mdelay = timedelta(0)


for x in xrange(1,10):
	def func1():
		call("./server")
	def func2():
		call("./client")

	tempo1 = datetime.now()
	Thread1 = threading.Thread(target = func1)
	Thread2 = threading.Thread(target = func2)
	
	Thread1.start()                                                                                                                                                     
	Thread2.start()

	Thread1.join()
	Thread2.join()
	tempo2 = datetime.now()      
	
	mdelay = mdelay + (tempo2 - tempo1)


print mdelay/10
