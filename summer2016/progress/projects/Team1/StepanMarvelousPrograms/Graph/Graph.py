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

sys.setrecursionlimit(25000)

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
				
				#  Uncomment this if you want only negative coefficients to stay
				if float(dependency[2]) < 0 :
					self.edges[dependency[0]][dependency[1]] = float(dependency[2])
				#---------------------------------------------------------------


				#  Comment this piece if you want directed graph
				#if dependency[1] not in self.edges :
				#	self.edges[dependency[1]] = {}
				#self.edges[dependency[1]][dependency[0]] = float(dependency[2])
				#-----------------------------------------------


				if dependency[1] not in self.incomingDegrees :
					self.incomingDegrees[dependency[1]] = 1
				else :
					self.incomingDegrees[dependency[1]] += 1
				self.genes.add(dependency[0])
				self.genes.add(dependency[1])
			
			#  uncomment this if you want to delete all one-sided links
			#unsuitableGenes = []
			#for gene in self.edges :
			#	for gene2 in self.edges[gene].keys() :
			#		if gene2 not in self.edges or gene not in self.edges[gene2].keys() :
			#			#index1 = self.edges[gene2].index(gene)
			#			#index2 = self.edges[gene].index(gene2)
			#			unsuitableGenes.append((gene, gene2))	
			#for pair in unsuitableGenes :
			#	self.edges[pair[0]].pop(pair[1]) 
			#----------------------------------------------------------
  
		print "  Graph initialized.\n"

	def transpose (self) :
		new = {}
		for gene in self.edges :
			for gene2 in self.edges[gene] :
				if gene2 not in new :
					new[gene2] = {}
				new[gene2][gene] = self.edges[gene][gene2]

		self.edges = dict(new)

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
	twiceVisitedVerticles = []
	names = []

	#  Uses depth-first search in order to find connected component of the graph 
	def calculateClusters (self, graph, filePath) :
		#   TODO: НОРМАЛЬНО РАЗБИТЬ НА ФУНКЦИИ
		self.names = list(graph.genes)
		i = len(self.names)-1

		with open(filePath, "w") as file :
			component = 0
			while i >= 0 :
				self._search (graph, self.names[i], file)

				component += 1
				
				clusterLen = i - len(self.names) + 1
				file.write("\nPrevious cluster ({})^\n\n".format(clusterLen))
				
				i = len(self.names)-1
			self.visitedVerticies = []
			self.names = []
			return component


	#  Depth-first search
	def search (self, graph, startVertex, outputFile) :
		self.names = list(graph.genes)
		self._search(graph, startVertex, outputFile)
		
		self.visitedVerticies = []
		self.names = []

	# It's private, dude
	def _search (self, graph, startVertex, outputFile) :
		index = self.names.index(startVertex)
		self.names.pop(index)
		self.visitedVerticies.append(startVertex)
		outputFile.write("{}\t".format(startVertex))
		if startVertex not in graph.edges :
			return
		for vertex in graph.edges[startVertex] :
			if vertex not in self.visitedVerticies :
				self._search(graph, vertex, outputFile)

	def __search (self, graph, startVertex, outputFile) :
		self.visitedVerticies.append(startVertex)
		outputFile.write("{}\t".format(startVertex))
		if startVertex not in graph.edges :
			return
		for vertex in graph.edges[startVertex] :
			if vertex not in self.visitedVerticies :
				self.__search(graph, vertex, outputFile)
	
	def searchNegative (self, graph, filePath) :
		self.names = []
		for gene in graph.genes :
			if gene not in graph.incomingDegrees.keys() :
				self.names.append(gene)

		i = len(self.names)-1

		with open(filePath, "w") as file :
			component = 0
			for gene in self.names :
				self.__search(graph, gene, file)
				file.write("\nPrevious cluster ({})^\n\n".format("fkf"))

			self.visitedVerticies = []
			self.names = []
			return component 

	#  Depth-first search
	def searchOriented (self, graph, filePath) :
		self.names = list(graph.genes)
		visited = set()
		timeStack = []

		for gene in self.names :
			if gene not in visited :
				self._specialOrientedSearch (graph, gene, visited, timeStack)

		visited = set()
		
		graph.transpose()
		
		with open(filePath, "w") as file : 
			for gene in reversed(timeStack) :
				self.__search (graph, gene, file)
				file.write ("\n It's kinda interlinked and stuff\n\n")

		self.visitedVerticies = []
		self.names = []

	# It's private, dude
	def _specialOrientedSearch (self, graph, startVertex, visited, timeStack) :
		visited.add(startVertex)
		if startVertex in graph.edges :
			for gene in graph.edges[startVertex] :
				if gene not in visited :
					self._specialOrientedSearch(graph, gene, visited, timeStack)
		timeStack.append (startVertex)


graph = GeneGraph("Cancer.txt")

searcher = Searcher()
print "Number of components: " + str(searcher.searchNegative(graph, "negativeClusters.lal"))



#degrees = fillDegrees(graph)

#showHistograms (degrees[0][::2], degrees[1][::2])

#analyseDataAndFindSickGenes (degrees[0], "IncomeSickCancerGenes.lal")
#analyseDataAndFindSickGenes (degrees[1], "OutcomeSickCancerGenes.lal")
