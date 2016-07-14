if __name__ == "__main__":
	lines = []
	meusIds = dict()

	with open("/Users/admin/Documents/UFRJ/SD/SD_2016.1/TrabalhoPratico3/Q2/output_1.txt", "rb") as file:
		lines = file.readlines()

	for line in lines:
		params = line.split(" ")

		if( (params[0] != "Meu") or (params[1] != "id:") or (params[3] != "meu") or params[4] != "tempo:"):
			print "Algo deu errado! Esta faltando palavras!"
			exit(0)

		else:
			if params[2] in meusIds:
				meusIds[params[2]] += 1
			else:
				meusIds[params[2]] = 1


	for v in meusIds.values():
		if (v != 100):
			print "Algo deu errado! Nao ha o numero de execucoes necessarias"
			exit(0)

	print "Tudo certo!"






