#!/usr/bin/env python

class Ambiente(object):
	mapa = []
	ouros = {}
	_debug = False
	def __init__(self, arq, debug):
		_debug = debug
		if debug :
			print "Inicializando Ambiente"
		self.n = int(arq[0])
		arqIndex = 2
		for i in range(self.n):
			j = 0
			tmp = []
			while arqIndex <= self.n*self.n + self.n and arq[arqIndex] != '\n':
				tmp.append(arq[arqIndex])
				arqIndex += 1
				j+=1
			self.mapa.append(tmp)
			if debug :
				print self.mapa[i][:self.n]
			arqIndex += 1
		for i in range (self.n):
			for j in range (self.n):
				self.ouros[(i,j)] = 0
		if debug :
			print "Ambiente inicializado"