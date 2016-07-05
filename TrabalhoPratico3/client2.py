import xmlrpclib
import sys
import time
from datetime import datetime, timedelta
from random import randrange

N = 10 #10^8
vector = [0]*N

if len(sys.argv) != 4:
    print "Verify the functions parameters.\n"
    exit(1)
else:
	K = int(sys.argv[1])
	order = int(sys.argv[2])  # 1 = Bulk arrival; 2 = Sequential arrival;


mdelay = timedelta(0)
tempo1 = datetime.now()

def write_file():


def send_to_coordinator(msg, myTime, myId):
	coordinator = xmlrpclib.ServerProxy('http://localhost:8000')
	#REQUEST
	if(msg == 1):
		coordinator.send_msg(msg, myTime, myId)
	#RELEASE
	elif(msg == 2):
		coordinator.send_msg(msg, myTime, myId)
	else:
		print "Operation not valid!"


if __name__ == "__main__":
	size = 10000000   # Number of random numbers to add
	procs = 2   # Number of processes to create

	processes = []
	for i in range(0, procs):
		p = multiprocessing.Process(target=send_to_coordinator, args=(msg, myTime, myId))
		processes.append(p)

	# Start the processes (i.e. calculate the random number lists)		
	for p in processes:
		p.start()

	# Ensure all of the processes have finished
	for p in processes:
		p.join()

	print "List processing complete."

tempo2 = datetime.now()   
mdelay = mdelay + (tempo2 - tempo1)
print mdelay

