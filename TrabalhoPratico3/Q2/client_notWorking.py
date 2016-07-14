import xmlrpclib
import sys
import time
from datetime import datetime, timedelta
import multiprocessing


if len(sys.argv) != 3:
    print "Verify the functions parameters.\n"
    exit(1)
else:
	K = int(sys.argv[1]) #number of client processes
	order = int(sys.argv[2])  # 1 = Bulk arrival; 2 = Sequential arrival;


mdelay = timedelta(0)
tempo1 = datetime.now()

def write_file(myTime, myId):
	with open("/Users/admin/Documents/UFRJ/SD/SD_2016.1/TrabalhoPratico3/Q2/log.txt", "a") as file:
		file.write("Meu id: " + str(myId) + ", meu tempo: " + str(myTime) + "\n")


def send_to_coordinator(myTime):
	coordinator = xmlrpclib.ServerProxy('http://localhost:8000')
	myId = p.pid
	myCount = 0
	while (myCount < 10):
		#REQUEST
		action = coordinator.ask_request(myTime, myId)
		if(action == 1):
			#received GRANT
			write_file(myTime, myId)
		myCount+=1
		#RELEASE
		print ("pq?")
		coordinator.printando()
		action = coordinator.send_release(myTime, myId)
		if (action == 1):
			time.sleep(1)



if __name__ == "__main__":
	processes = []
	for i in range(0, K):
		p = multiprocessing.Process(target=send_to_coordinator, args=(  (str(datetime.now()),))  )
		processes.append(p)

		
	for p in processes:
		p.start()

	for p in processes:
		p.join()

	print "List processing complete."

tempo2 = datetime.now()   
mdelay = mdelay + (tempo2 - tempo1)
print mdelay

