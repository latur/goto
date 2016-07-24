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


#  Read and parse data from file
data = open ("reads.fa").readlines()
reads = []
for line in data : 
	if line[0] == '>': continue
	else: reads.append (line.replace('\n', ''))

def transpose (read) :
	change = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}

	lenSz = len(read)
	transposedRead = ""

	for i in range (lenSz) :
		transposedRead += change[read[i]]

	return transposedRead


#  Translates nucleotide lines into protin lines with chosen shift(for frame)
def translateToProteins (read, shift) :
	proteins = {"AAA":"K", "AAC":"N", "AAG":"K", "AAT":"N", "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
	            "AGA":"R", "AGC":"S", "AGG":"R", "AGT":"S", "ATA":"I", "ATC":"I", "ATG":"M", "ATT":"I",
	            "CAA":"Q", "CAC":"H", "CAG":"Q", "CAT":"H", "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
	            "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R", "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
	            "GAA":"E", "GAC":"D", "GAG":"E", "GAT":"D", "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
	            "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G", "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
	            "TAA":".", "TAC":"Y", "TAG":".", "TAT":"Y", "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
	            "TGA":".", "TGC":"C", "TGG":"W", "TGT":"C", "TTA":"L", "TTC":"F", "TTG":"L", "TTT":"F"}

	line = ""

	shift = shift%3
	for i in range (shift, len (read)+shift-3) :
		triplet = read[i: i+3]
		if triplet not in proteins :
			line += "~"
		else :
			line += proteins[triplet]
	return line

#  Make columns of letters with same position using very convinient sets
def makeColumns (amynoReads) :
	columns = []
	for i in range (len (amynoReads[0])) :
		columns.append([])
		for read in amynoReads :
			columns[i].append (read[i])
	for i in range (len (columns)) :
		columns[i] = set (columns[i])
	return columns

#  Leave only invariant proteins among all reads 
def cutAllMutations (columns) :
	result = ""
	for column in columns :
		if len (column) == 1 :
			result += column.pop()
		else :
			result += "_"
	return result


#  Better than slice
class exon :
	leftSide = -228
	rightSide = -228
	
	def __init__(self, leftSide, rightSide):
		self.leftSide  = leftSide
		self.rightSide = rightSide

#  Exons only allowed here
#  I LOVE SWIFT
def exonDistance (tot, etot) :
	return tot.leftSide-etot.rightSide
 
def findExons (unmutatedReads) :
	minExonLength = 8

	exonCoords = [[], [], []]
	str = ""

	tempExons = [[0,""], [0,""], [0,""]]
	for i in range (len(unmutatedReads[0])) :
		for j in range (3) :
			if unmutatedReads[j][i] not in ['~', '_'] :
				if tempExons[j][1] == "" :
					tempExons[j] = [i, unmutatedReads[j][i]]
				else : 
					tempExons[j][1] += unmutatedReads[j][i]
			else :
				if len(tempExons[j][1]) > minExonLength :
					#exonCoords[j].append ([tempExons[j][0], i-1])
					str += "{}\t{}\n".format(tempExons[j][0]*3, (i-1)*3)
					tempExons[j] = [0, ""]
	print str

results = []

#  Can be optimized from 'fast' to 'fast as hell' but i'm too lazy
for i in range(3) :
	translatedData = []

	for read in reads :
		#  Игорь спалил... аналитически выявлено
		transposed = transpose(read)
		translatedData.append (translateToProteins (transposed, i))

	amynoColumns = makeColumns (translatedData)

	result = cutAllMutations (amynoColumns)
	results.append(result)

findExons(results)

