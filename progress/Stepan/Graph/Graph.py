#!/usr/bin/python
# -*- coding: utf-8 -*-
'''                                ______                         
		                     _.-*'"      "`*-._                   
		                _.-*'                  `*-._              
		             .-'                            `-.           
		  /`-.    .-'                  _.              `-.        
		 :    `..'                  .-'_ .                `.      
		 |    .'                 .-'_.' \ .                 \     
		 |   /                 .' .*     ;               .-'"     
		 :   L                    `.     | ;          .-'         
		  \.' `*.          .-*"*-.  `.   ; |        .'            
		  /      \        '       `.  `-'  ;      .'              
		 : .'"`.  .       .-*'`*-.  \     .      (_               
		 |              .'        \  .             `*-.           
		 |.     .      /           ;                   `-.        [SO FUCKIN FAST]
		 :    db      '       d$b  |                      `-.     
		 .   :PT;.   '       :P"T; :                         `.   
		 :   :bd;   '        :b_d; :                           \  
		 |   :$$; `'         :$$$; |                            \ 
		 |    TP              T$P  '                             ;
		 :                        /.-*'"`.                       |
		.sdP^T$bs.               /'       \                       
		$$$._.$$$$b.--._      _.'   .--.   ;                      
		   \                        .'   ; ;              
		    `.                  _.-'    ' /                       
		      `*-.                      .'                        
		          `*-._            _.-*'                          
		               `*=--..--=*'
'''

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

class GeneGraph :
	edges = {}
	incomingDegrees = {}
	genes = set()

	#  Data = {name: {name: expressionCoefficient}}
	#  Dalues = {name: value}
	def __init__ (self, filePath) :#, values) :
		with open (filePath) as file :
			for line in file :
				dependency = line.strip().split()
				if dependency[0] not in self.edges :
					self.edges[dependency[0]] = {}
				self.edges[dependency[0]][dependency[1]] = float(dependency[2])
				
				if dependency[1] not in self.incomingDegrees :
					self.incomingDegrees[dependency[1]] = 1
				else :
					self.incomingDegrees[dependency[1]] += 1
				self.genes.add(dependency[0])
				self.genes.add(dependency[1])

	#  Return number of outcoming dependencies of a particular gene in graph.
	def getOutcomingDegreeOfGene (self, geneName) :
		if geneName not in self.edges :
			return 0
		else :
			return len(self.edges[geneName]) 

	#  Return number of incoming dependencies of a particular gene in graph.
	def getIncomingDegreeOfGene (self, geneName) :
		if geneName not in self.incomingDegrees :
			return 0
		else :
			return self.incomingDegrees[geneName]

def fillDependencies (graph) :
	incomingDegreesForGraph = []
	for gene in graph.genes :
		incomingDegreesForGraph.append(graph.getIncomingDegreeOfGene(gene))

	outcomingDegreesForGraph = []
	for gene in graph.genes :
		outcomingDegreesForGraph.append(graph.getOutcomingDegreeOfGene(gene))

	return (incomingDegreesForGraph, outcomingDegreesForGraph)

def showHistograms (incomingDegreesForGraph, outcomingDegreesForGraph) :
	plt.subplot (2,1,0)
	plt.hist(incomingDegreesForGraph, bins = 60)
	plt.subplot (2,1,1)
	plt.hist(outcomingDegreesForGraph, bins = 60)
	plt.show()

def calculateThreshold(degrees) :
	avg = np.mean(degrees)
	standartDeviation = 0
	for value in degrees :
		squareDeviation = pow(value-avg, 2)
		standartDeviation += squareDeviation
	
	standartDeviation /= len(degrees)
	standartDeviation = sqrt(standartDeviation)

	threshold = avg + 2*standartDeviation
	return threshold
	
graph = GeneGraph("HumanNet.txt")

degrees = fillDependencies(graph)

#showHistograms(degrees[0], degrees[1])
print calculateThreshold(degrees[0])
print calculateThreshold(degrees[1])
