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
import sys

sys.setrecursionlimit(15000)

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
				
				#  Comment this piece if you want directed graph
				if dependency[1] not in self.edges :
					self.edges[dependency[1]] = {}
				self.edges[dependency[1]][dependency[0]] = float(dependency[2])
				#-----------------------------------------------


				if dependency[1] not in self.incomingDegrees :
					self.incomingDegrees[dependency[1]] = 1
				else :
					self.incomingDegrees[dependency[1]] += 1
				self.genes.add(dependency[0])
				self.genes.add(dependency[1])
		print "  Graph initialized.\n"

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

#  Calculates income and outcome degrees for each gene and puts them to two arrays
def fillDegrees (graph) :
	incomingDegreesForGraph = []
	for gene in graph.genes :
		incomingDegreesForGraph.append(graph.getIncomingDegreeOfGene(gene))
		incomingDegreesForGraph.append(gene)

	outcomingDegreesForGraph = []
	for gene in graph.genes :
		outcomingDegreesForGraph.append(graph.getOutcomingDegreeOfGene(gene))
		outcomingDegreesForGraph.append(gene)		

	return (incomingDegreesForGraph, outcomingDegreesForGraph)
	print "  Degrees calculated.\n"
 

#  Makes histograms for each degree array
def showHistograms (incomingDegreesForGraph, outcomingDegreesForGraph) :
	plt.subplot (2,1,0).set_title("Income")
	plt.hist(incomingDegreesForGraph, bins = 60)
	plt.subplot (2,1,1).set_title("Outcome")
	plt.hist(outcomingDegreesForGraph, bins = 60)
	plt.show()

#  Some statistics manipulations to get the outstanding degree values
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

#  Sick - crazy, cool, insane (urbandictionary.com).
def findSickGenes (degrees, threshold) :
	result = ""
	for i in range (0, len(degrees), 2) :
		if degrees[i] >= threshold :
			result += "{}\t{}\n".format(degrees[i+1], degrees[i])
	return result

#  Creates file on selected path and puts data into it
def saveToFile (path, data) :
	with open(path, "w") as result :
		result.write(data)
		print ("  File \"{}\" created.").format(path)

#  Calculates and saves all stuff
def analyseDataAndFindSickGenes (degrees, path) :
	treshold = calculateThreshold(degrees[::2]) 
	print "  Threshold calculated."
	
	sickGenes = findSickGenes(degrees, treshold)
	saveToFile (path, sickGenes)

class Searcher :
	visitedVerticies = []
	names = []

	#  Uses depth-first dearch in order to find connected component of the graph 
	def startSearch (self, graph) :
		#   TODO: НОРМАЛЬНО РАЗБИТЬ НА ФУНКЦИИ
		self.names = list(graph.genes)
		i = len(self.names)-1

		with open("indirectedClusters.lal", "w") as file :
			component = 0
			while i >= 0 :
				self._search (graph, self.names[i], file)
				component += 1
				
				clusterLen = i - len(self.names) + 1
				file.write("\nPrevious cluster ({})^\n\n".format(clusterLen))
				
				i = len(self.names)-1
			return component


	# It's private, dude.
	def _search (self, graph, startVertex, fileForWriting) :
		index = self.names.index(startVertex)
		self.names.pop(index)
		self.visitedVerticies.append(startVertex)

		fileForWriting.write("{}\t".format(startVertex))
		if startVertex not in graph.edges :
			return
		for vertex in graph.edges[startVertex] :
			if vertex not in self.visitedVerticies :
				self._search(graph, vertex, fileForWriting)



graph = GeneGraph("Cancer.txt")

searcher = Searcher()
print "Number of components: " + str(searcher.startSearch(graph))

#degrees = fillDegrees(graph)

#showHistograms (degrees[0][::2], degrees[1][::2])

#analyseDataAndFindSickGenes (degrees[0], "IncomeSickCancerGenes.lal")
#analyseDataAndFindSickGenes (degrees[1], "OutcomeSickCancerGenes.lal")
