#!/usr/bin/python
# coding=utf-8

import csv

with open("Scouts.csv", "r") as csvfile:
	orig = csv.reader(csvfile)
	dest = csv.writer(open("Scouts2.csv", "w"))
	dest.writerow(["Atleta", "Pontos", "Media", "Preco atual", "Preco var", "FS","PE","A","FT","FD","FF","G","I","PP","RB","FC","GC","CA","CV","SG","DD","DP","GS"])
	dic = dict()
	for linha in orig:
		if linha[3] == "1":
			linhaAux = []
			i = 5
			while i < 10: # linhaAux[0:5]
				linhaAux.append(float(linha[i]))
				i += 1
			i = 16
			l = len(linha)
			soma = 0
			while i < l: # linhaAux[5:] = ...
				linhaAux.append(int(linha[i]))
				soma += int(linha[i])
				i += 1
			if linha[6] == "0" or soma != 0:
				if linha[0] not in dic:
					dic[linha[0]] = linhaAux[5:]
				else:
					i = 0
					l = len(dic[linha[0]])
					while i < l:
						dic[linha[0]][i] = dic[linha[0]][i] + linhaAux[5+i]
						i += 1
				scouts = list()
				nJogos = linhaAux[0]
				i = 0
				l = len(linhaAux)
				while i < l-5:
					scouts.append(float(dic[linha[0]][i])/nJogos)
					i += 1
				dest.writerow([linha[0], linha[6]] + linhaAux[2:5] + scouts)