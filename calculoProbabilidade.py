#!/usr/bin/python
# coding=utf-8

import csv
import numpy as np
import math

def gauss(x, u, s2):
	return math.exp(-( (x-u)**2)/(2*s2) )/(math.sqrt(math.pi*2*s2))

with open("Tabela.csv", "r",  encoding="utf8") as csvfile:
	arq = csv.reader(csvfile)
	variaveis = dict()
	variaveis["MediaS"] = list()
	variaveis["DesvioS^2"] = list()
	variaveis["MediaN"] = list()
	variaveis["DesvioN^2"] = list()
	variaveis["P(S)"] = list()
	variaveis["P(N)"] = list()
	variaveis["nInstancias"] = list()
	for linha in arq:
		if linha[0] != "Variavel":
			for item in linha[1:]:
				variaveis[linha[0]].append(float(item))

entrada = [0.0,5.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0]

probS = 1.0
i = 0
l = len(entrada)
while i < l:
	probS *= gauss(entrada[i], variaveis["MediaS"][i], variaveis["DesvioS^2"][i])
	i += 1
probS*= variaveis["P(S)"][0]
print(probS)

probN = 1.0
i = 0
while i < l:
	probN *= gauss(entrada[i], variaveis["MediaN"][i], variaveis["DesvioN^2"][i])
	i += 1
probN*= variaveis["P(N)"][0]
print(probN)

print("Probabilidade S: %.3f" %(probS/(probS+probN)))
print("Probabilidade N: %.3f" %(probN/(probS+probN)))