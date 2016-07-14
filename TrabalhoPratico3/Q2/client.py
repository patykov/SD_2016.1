import rpyc
import sys
import time
import random
from datetime import datetime, timedelta
import multiprocessing


if len(sys.argv) != 3:
    print "Verify the functions parameters.\n"
    exit(1)
else:
	K = int(sys.argv[1]) #number of client processes
	order = int(sys.argv[2])  # 1 = Bulk arrival; 2 = Sequential arrival;


def write_file(myTime, myId):
	with open("/Users/admin/Documents/UFRJ/SD/SD_2016.1/TrabalhoPratico3/Q2/output.txt", "a") as file:
		file.write("Meu id: " + str(myId) + ", meu tempo: " + str(myTime) + "\n")

def write_final_time(Time):
	with open("/Users/admin/Documents/UFRJ/SD/SD_2016.1/TrabalhoPratico3/Q2/log.txt", "a") as file:
		file.write("Numero de processos: " + str(K) + ", ordem: " + str(order) + "\nMeu tempo: " + str(Time) + "\n")
		file.write("_________________________________________________________________\n")


def send_to_coordinator(myTime):
	coordinator = rpyc.connect("localhost", 18860)
	myId = p.pid
	myCount = 0
	while (myCount < 100):
		#REQUEST
		action = coordinator.root.exposed_ask_request(myTime, myId)
		if(action == 1):
			#GRANT received
			write_file(myTime, myId)
		myCount+=1
		#RELEASE
		action = coordinator.root.exposed_send_release(myTime, myId)
		if (action == 1):
			time.sleep(round(random.random(),1))
			myTime = str(datetime.now())



if __name__ == "__main__":

	mdelay = timedelta(0)
	tempo1 = datetime.now()
	processes = []
	for i in range(0, K):
		p = multiprocessing.Process(target=send_to_coordinator, args=(  (str(datetime.now()),))  )
		processes.append(p)

	#Bulk Arrival
	if (order == 1):
		for p in processes:
			p.start()

	#Sequencial Arrival
	elif (order == 2):
		for p in processes:
			p.start()
			time.sleep(1)
	for p in processes:
		p.join()


	tempo2 = datetime.now()   
	mdelay = mdelay + (tempo2 - tempo1)
	write_final_time(mdelay)

