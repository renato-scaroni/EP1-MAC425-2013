#!/usr/bin/env python

class Agente(object):
	_debug = False
	estadosVisitados = [] #lista de tuplas 
	o = [] #Ouros coletados

	#Funcao que realiza a busca em largura 
	def BFS (self, mina, n, g):
		print "Iniciando busca com BFS"
		curr = 0, 0
		fila = []
		o = []
		fila.append(curr)
		while (len(fila) > 0):
			curr = fila[0]
			del(fila[0])
			if(curr == (0,0)) and (len(o) == g):
				print "esatdo final, saindo "+str(curr) + str(o)
				break
			if(mina.mapa[curr[0]][curr[1]] == '*'):
				o.append(curr)
			self.estadosVisitados.append((curr, (o[i] for i in range(len(o)))))
			print"curr: " + str(curr)
			print "ouros: " + str(o)
			print "estadosVisitados: "+ str(self.estadosVisitados)
			for d in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
				next = curr[0] + d[0], curr[1] + d[1]
				if not (next, o) in self.estadosVisitados:
					if (next[0] >= 0 and next[0] < n) and (next[1] >= 0 and next[1] < n):
						if not mina.mapa[next[0]][next[1]] == '1':
							fila.append(next)


	def __init__(self, debug):
		if debug :		
			_debug = debug
			print "Agente criado"

