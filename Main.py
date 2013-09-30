#!/usr/bin/env python

import sys
import Agente
import Ambiente
 
class Main:
	def main (self):
		if len(sys.argv) < 3 or len(sys.argv) > 4:
			print "Formato de entrada errado. Formato correto: \n./executavel <-d>(Opcao de debug, opcional) <nome_do_arquivo> <tipo_de_busca>"
			return

		DEBUG = False
		if len(sys.argv) == 4 :
			if sys.argv[1] == "-d" :
				DEBUG = True
			else :
				print "Formato de entrada errado. Formato correto: \n./executavel <-d>(Opcao de debug, opcional) <nome_do_arquivo> <tipo_de_busca>"
				print "opcao incorreta, digite -d para debug mode ou nada para normal mode"
				return

		if DEBUG :
			print "Iniciando programa"

		agente = Agente.Agente(DEBUG)

		if DEBUG :
			print "arquivo de entrada: " + sys.argv[2]
			ambiente = Ambiente.Ambiente(open(sys.argv[2], "r").read(), DEBUG)
		else:
			ambiente = Ambiente.Ambiente(open(sys.argv[1], "r").read(), DEBUG)

		agente.BFS(ambiente, ambiente.n, 1)

main  = Main()

main.main ()
