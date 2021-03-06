#!/usr/bin/env python

class Agente(object):
	_debug = False

	def GetDirFromDiff(self, d):
		delta = [[0, 1], [1, 0], [-1, 0], [0, -1]]
		direc = ['D', 'B', 'C', 'E']
		for i, j in zip(delta, direc):
			if(i[0] == d[0] and i[1] == d[1]):
				return j
		return '?'		

	def GetDirFromVecs(self, b, c):
		x = c[0] - b[0]
		y = c[1] - b[1]
		delta = [[0, 1], [1, 0], [-1, 0], [0, -1]]
		direc = ['D', 'B', 'C', 'E']
		for i, j in zip(delta, direc):
			if(i[0] == x and i[1] == y):
				return j
		return '?'

	def BuildPath(self, parnt, s, f):
		v = f
		path = []
		custo = 0
		# path = [v]
		# print f
		while not v == parnt[v]:
			path.append(self.GetDirFromVecs(parnt[v], v))
			# path.append(parnt[v])
			v = parnt[v]
			custo -= 1
		path.reverse()
		return custo, path

	#Funcao que realiza a busca em largura 
	def BFS (self, mina, n, g):
		print "Iniciando busca com BFS g=" + str(g)
		curr = 0, 0
		fila = []
		o = []
		estadosVisitados = [] #lista de tuplas 
		fila.append(curr)
		path = []
		tmpPath = []
		s = 0, 0
		parnt = {}
		parnt[(0,0)] = (0,0)
		custo = 0
		while (len(fila) > 0):
			curr = fila.pop(0)
			if(curr == (0,0)) and (len(o) == g):
				ret = self.BuildPath(parnt, s, curr)
				path += ret [1]
				custo += ret[0]
				if self._debug :
					print "estado final, saindo "+str(curr) + str(o)
				break
			if(mina.mapa[curr[0]][curr[1]] == '*' and not curr in o and len(o) < g):
				ret = self.BuildPath(parnt, s, curr)
				path += ret [1]
				custo += ret[0]
				s = curr
				parnt[s] = s
				path += 'P'
				custo += 4*n
				o.append(curr)
			estadosVisitados.append((curr, []))
			for a in o:
				estadosVisitados[-1][1].append(a)
			if self._debug :
				print"curr: " + str(curr)
				print "ouros: " + str(o)
				print "estadosVisitados: "+ str(estadosVisitados)
			for d in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
				next = curr[0] + d[0], curr[1] + d[1]
				if not (next, o) in estadosVisitados:
					if (next[0] >= 0 and next[0] < n) and (next[1] >= 0 and next[1] < n):
						if not mina.mapa[next[0]][next[1]] == '1':
							parnt[next] = curr
							# print str(curr) + "->" + str(next)
							fila.append(next)
		return custo, path

	def __init__(self):
		self._debug  = False

	def __init__(self, debug):
		if debug :		
			self._debug = debug
			print "Agente criado"

def GetTestObj():
	return Agente(True)

