from subprocess import call
import datetime
from datetime import timedelta
import time

def break_line(k, order):
	with open("/Users/admin/Documents/UFRJ/SD/SD_2016.1/TrabalhoPratico3/Q2/log_do_script.txt", "a") as file:
		file.write("___________________________________________ \n")
		file.write("Numero de processos: " + str(k) + ", Operacao: " + str(order) + "\n")


for k in [128]: #[1, 2, 4, 8, 16, 32, 64, 128]:
	for order in [2]: #[1, 2]:
		break_line(k, order)
		for x in range(1,10):
			call("python rpyc_client.py " + str(k) + " " + str(order), shell=True)
		



