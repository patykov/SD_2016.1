from subprocess import call
import datetime
from datetime import timedelta

def break_line(k, op):
	with open("/Users/admin/Documents/UFRJ/SD/SD_2016.1/TrabalhoPratico3/log.txt", "a") as file:
		file.write("___________________________________________ \n")
		file.write("Numero de threads: " + str(k) + " Operacao: " + str(op) + "\n")


for k in [1, 2, 4, 8, 16, 32, 64, 128]:
	for op in [1, 2, 3]:
		break_line(k, op)
		for x in range(1,10):
			call("python client.py " + str(k) + " " + str(op) + " 2", shell=True)
		



