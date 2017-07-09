#!/usr/bin/python
# coding=utf-8

import csv
import numpy as np
import math

with open("Scouts2.csv", "r",  encoding="utf8") as csvfile:
	arq = csv.reader(csvfile)
	somaS = np.array([0.0]*21)
	nS = 0
	matrisS = list()
	somaN = np.array([0.0]*21)
	nN = 0
	matrisN = list()
	for linha in arq:
		if len(linha) != 0 and linha[1] != "Pontos":
			i = 2
			l = len(linha)
			linhaAux = []
			while i < l:
				linhaAux.append(float(linha[i]))
				i += 1
			if float(linha[1]) >= 8: # mitou
				matrisS.append(linha[2:])
				somaS += np.array(linhaAux)
				nS += 1
			else: # não mitou
				matrisN.append(linha[2:])
				somaN += np.array(linhaAux)
				nN += 1

	mediaS = somaS/nS
	mediaN = somaN/nN

	soma = np.array([0.0]*21)
	for line in matrisS:
		i = 0
		l = len(line)
		linhaAux = []
		while i < l:
			linhaAux.append(float(line[i]))
			i += 1
		soma += (np.array(linhaAux)-mediaS)**2
	desvioS = soma/nS

	soma = np.array([0.0]*21)
	for line in matrisN:
		i = 0
		l = len(line)
		linhaAux = []
		while i < l:
			linhaAux.append(float(line[i]))
			i += 1
		soma += (np.array(linhaAux)-mediaN)**2
	desvioN = soma/nN

	dest = open("Tabela.csv", "w")
	dest.write("Variavel,Media,Preco atual,Preco var,FS,PE,A,FT,FD,FF,G,I,PP,RB,FC,GC,CA,CV,SG,DD,DP,GS\n")
	dest.write("MediaS,")
	for item in mediaS[:-1]:
		dest.write(str(item) + ",")
	dest.write(str(mediaS[-1]))
	dest.write("\n")
	dest.write("DesvioS^2,")
	for item in desvioS[:-1]:
		dest.write(str(item) + ",")
	dest.write(str(desvioS[-1]))
	dest.write("\nP(S)," + str(nS/(nN+nS)) + "\n")

	dest.write("MediaN,")
	for item in mediaN[:-1]:
		dest.write(str(item) + ",")
	dest.write(str(mediaN[-1]))
	dest.write("\n")
	dest.write("DesvioN^2,")
	for item in desvioN[:-1]:
		dest.write(str(item) + ",")
	dest.write(str(desvioN[-1]))
	dest.write("\nP(N)," + str(nN/(nN+nS)) + "\nnInstancias," + str(nN+nS))