f=open('D://projects/reads1.txt')
line = f.read()
e = line.split('\n')
e.pop()

e = e[1::2]
for i in range(0,len(e)):
	for ch in e[i]:
		if(ch == 'A'): ch = 'T'
		if(ch == 'T'): ch = 'A'
		if(ch == 'G'): ch = 'C'
		if(ch == 'C'): ch = 'G'
	e[i][::-1]	    #разврачиваем последовательность


amin = {
	'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
	'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I', 
	'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
	'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
	'TAA':'.', 'TAC':'Y', 'TAG':'.', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
	'TGA':'.', 'TGC':'C', 'TGG':'W', 'TGT':'C', 'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F' 
}
mutAminCount = {
			'K' : 0,
			'N' : 0,
			'T' : 0,
			'R' : 0,
			'S' : 0,
			'I' : 0,
			'M' : 0,
			'H' : 0,
			'Q' : 0,
			'P' : 0,
			'L' : 0,
			'E' : 0,
			'D' : 0,
			'D' : 0,
			'A' : 0,
			'G' : 0,
			'V' : 0,
			'Y' : 0,
			'.' : 0,
			'C' : 0,
			'W' : 0,
			'F' : 0,
}
nach_end_arr = []
for z in range(3):
	mutAmin = []
	for i in range(0,len(e)):
		mutAmin.append("")
		for j in range(z,len(e[0])-z-2,3):
			if (e[i][j]=='A' or e[i][j]=='T' or e[i][j]=='G' or e[i][j]=='C') and not 'N' in e[i][j:j+3]:
				str = e[i][j:j+3]
				aminNow = amin[str]
				mutAmin[i]+=aminNow
			else: 
					str = 'n'   #переводим в аминокислоты
					continue	

	#print(mutAmin)

	#mutAmin -> MAIN

	mutCount = [] #mutCount{столбец : nuc{e[j][i] : count} }
	#print(len(mutAmin[1000]), '\n', len(mutAmin))
	for i in range(0,len(mutAmin[0])) :    #выводит словарь, в котором есть количество каждой аминокислоты в столбце
		mutAminCountCopy =  {}
		mutAminCountCopy = mutAminCount.copy()
		for j in range(0, len(mutAmin)):
			#print(j , '\t' , i , '\t' ,mutAmin[j][i])
			nowAmin = mutAmin[j][i]
			mutAminCountCopy[nowAmin] = mutAminCountCopy[nowAmin]+1
		mutCount.append(mutAminCountCopy)
		del(mutAminCountCopy)
	#print(mutCount)

	#mutCount -> MAIN

	is_ex_ar = []
	is_ex = 0
	for i in range(0,len(mutCount)):  #делает бинарный массив. 1 - нет мутации в столбце. 0 - есть мутация
		is_ex = 0
		for k,v in mutCount[i].items():
			if v == 1000:
				is_ex = 1
		is_ex_ar.append(is_ex)
	#print(is_ex_ar)			


	nach_end = {}
	longMax = 0
	nach = 0
	print(len(is_ex_ar), '\t', len(mutAmin[0]), '\n') #перевод бинарного массива в промежутки - места нахождения экзонов
	for i in range(0, len(is_ex_ar)):
		if is_ex_ar[i] == 1:
			if longMax == 0:
				nach = i*3-1
			longMax+=1		
		else:
			if longMax>=4:
				nach_end[nach] = i*3
				#print(nach, '\t', is_ex_ar[i], '\n')
			nach = 0
			longMax = 0

	nach_end_arr.append(nach_end)
exons_arr = []		
for k,v in nach_end_arr[2].items():  #было влом выводить для всех сразу, вывожу по одному варианту (всего 3 варианта из-за сдвига)
	exons_arr.append(k)		#просто вывод промежутков в удобном виде
	exons_arr.append(v)

exons_arr.sort()
for i in range(0,len(exons_arr), 2):
	print(exons_arr[i], '\t', exons_arr[i+1], '\n')

'''
sovCoint = 15486
sovCointNow = 0
sovNumStr = 0
idStr = e[0]
numRaznCharsNow = []
numRaznChars = []
for i in range(0,len(e)): #изначальная строка
	sovCoint = 15486
	for j in range(i,len(e)): #сравниваемая строка
		sovCointNow = 0
		for k in range(0,len(e[0])):
			if(e[i][k] != e[j][k]):
				sovCointNow+=1
				numRaznCharsNow.append(k)
	
		if(sovCointNow<sovCoint):
			sovCoint = sovCointNow
			sovNumStr = j
			numRaznChars = numRaznCharsNow
		numRaznCharsNow = []	


	for i in range(0, len(numRaznChars)):
		idStr[i] = e[sovNumStr][i]

print(idStr)			
'''

