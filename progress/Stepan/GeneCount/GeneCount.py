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
geneList = [[],[]]
blankNames = {}
with open("genes.txt") as f :
	for line in f :
		line = eval(line)
		if line [2] == "-" :
			geneList[0].append(line)
		else :
			geneList[1].append(line)
		blankNames[line[3]] = 0
geneListSz = [len(geneList[0]), len(geneList[1])]
print ("parsed")

#  Find gene that intersects with gene part
def findGene (genePart, len, complimentary, lastPos, names) :
	#print lastPos
	gene = [0,0, ""]

	if lastPos is None :
		return lastPos

	for i in range(lastPos, geneListSz[complimentary]):
		gene = [int(geneList[complimentary][i][0]), int(geneList[complimentary][i][1]), geneList[complimentary][i][3]]
		
		if genePart+len-1 < gene[0] :
			#print lastPos, i
			if i >= 3 :
				return (i-3)
			else : 
				return 0
		else :
			if genePart > gene[1] :
				continue
			
			#geneRange = range (gene[0], gene[1])

			if ((gene[1] > genePart and genePart > gene[0]) or (gene[1] > (genePart+len-1) and (genePart+len-1) > gene[0])) :
				names[gene[2]] += 1
				if i >= 3 :
					#print lastPos, i
					return (i-3)
				else : 
					#print lastPos, i
					return 0
			else :
				continue
		


#  Find gene direction (reverse comlimentary or straight)
def getStrand (val) :
	if (val & 16) :
		return 0
	else :
		return 1

def count (filename) :
	tempNames = {}
	for key in blankNames.keys() :
		tempNames[key] = 0
	with open(filename) as geneParts :
		len = 51
		lastPos = [0,0]
		i = 0
		for line in geneParts :
			line = line.strip().split()
			strand = getStrand(int(line[1]))
			pos = int(line[3])
			lastPos[strand] = findGene(pos, len, strand, lastPos[strand], tempNames)

			i += 1

			if (i%100000 == 0) :
				print i
			#print lastPos 
		return tempNames

first  = count ("PolyplusN1.22chr.sorted.sam")
print "first file counted."
second = count ("PolyplusH1.22chr.sorted.sam")

with open ("result.lal", "w") as result :
	for name in blankNames.keys() :
		result.write(name.replace("\"", ""))
		result.write("\t{}\t{}\n".format(first[name], second[name]))


