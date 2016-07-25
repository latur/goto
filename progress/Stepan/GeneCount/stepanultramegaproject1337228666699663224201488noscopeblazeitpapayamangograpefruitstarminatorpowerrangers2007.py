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

#  Parsing
genes = {}
with open ("result.lal") as file :
	for line in file :
		line = line.strip().split()
		genes[line[0]] = (int(line[1]), int(line[2]))
print "parsed."

#  Calculating weird formula for expression difference(kinda)
def calculateDifference (gene, minDifference) :
	deltaN = gene[1]-gene[0]
	positiveness = None
	if abs(deltaN) <= minDifference:
		return 0
	else :
		result = None
		if gene[0] == 0 :
			#  Забыл зачем это
			result = float(gene[1]-1)/float(gene[1]+1)
		else : 
			result = float(gene[1]-gene[0])/float(gene[1]+gene[0])
		return result

#  Made for vanishing copypast
def saveFile (path, data) :
	with open("path", "w") as f :
		f.write(data)
	print "file \"{}\" saved.".format(path)

minDiff = 20
differences = {}
for currentGene in genes.keys() :
	diff = calculateDifference(genes[currentGene], minDiff)
	if diff not in differences :
		differences[diff] = [currentGene]
	else :
		differences[diff].append(currentGene)

sortedValues = sorted(differences.keys())
topMin = ""
topMax = ""

# Мерзкий копипаст
for value in sortedValues[:50] :
	topMin += str(value)
	for i in range(len(differences[value])) :
		topMin += "\t{}".format(differences[value][i])
	topMin += "\n"

length = len(sortedValues)

for i in range(50) :
	value = sortedValues[length-1-i]
	topMax += str(value)
	for i in range(len(differences[value])) :
		topMax += "\t{}".format(differences[value][i])
	topMax += "\n"

saveFile ("topMax.lal", topMax)
saveFile ("topMin.lal", topMin)