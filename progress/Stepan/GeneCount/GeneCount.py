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
names = {}
with open("genes.txt") as f :
	for line in f :
		line = eval(line)
		if line [2] == "-" :
			geneList[0].append(line)
		else :
			geneList[1].append(line)
		names[line[3]] = 0

print ("parsed")

#  Find gene that intersects with gene part
def findGene (genePart, len, complimentary, lastPos) :
	print len(geneList[complimentary])
	for i in range(lastPos, len(geneList[complimentary])):
		genePart = geneList[complimentary][i]
		if (genePart in range (int(gene[0]), int(gene[1]) or (genePart+len-1) in range (int(gene[0]), int(gene[1])))) :
			names[gene[3]] += 1
			return (i-3)


#  Find gene direction (reverse comlimentary or straight)
def getStrand (val) :
	if (val & 16) :
		return 0
	else :
		return 1

with open("PolyplusH1.22chr.sorted.sam") as geneParts :
	len = 51
	lastPos = [0,0]
	for line in geneParts :
		line = line.strip().split()
		strand = getStrand(int(line[1]))
		pos = int(line[3])
		lastPos[strand] = findGene(pos, len, strand, lastPos[strand]) 

print (names)

#with open ("result.lal", "w") as result :
	#result = names
	#print ("results saved")
