f=open('D://projects/files/NewHumanNet.txt')
f1=open('D://projects/files/Cancer_MEL_Network.txt')
genArrH = {} #{ out: [ in ] }
genArrC = {} #{ out: [ {in:expr}, ... ] }
for  line in f:
	if line == "":
		break
	lineAr = line.strip().split('\t')
	#print(lineAr)
	if lineAr[0] not in genArrH:
		genArrH[lineAr[0]] = []
	if lineAr[1] not in genArrH:
		genArrH[lineAr[1]] = []	
	genArrH[lineAr[0]].append(lineAr[1])


for line in f1:
	if line == "":
		break
	lineAr = line.strip().split('\t')
	lineAr[2] = float(lineAr[2])
	reb = {}
	reb[lineAr[1]] = lineAr[2]
	if lineAr[0] not in genArrC:
		genArrC[lineAr[0]] = []
	if lineAr[1] not in genArrC:
		genArrC[lineAr[1]] = []	
	genArrC[lineAr[0]].append(reb)
#print(genArrH)		
#print(genArrC)

setH = set()
setC = set()
for k,v in genArrH.items():
	setH.add(k)
for k,v in genArrC.items():
	setC.add(k)

reparated = setC.intersection(setH)

genH = {}
genC = {}
for i in reparated:
	if i in genArrC:
		genC[i] = genArrC[i]  #{ outName: [ inName ] }
	if i in genArrH: 
		genH[i] = genArrH[i]  #{ outName: [ {inName : expr}, ... ] }
diffMap = {}		
diffArr = []	
for k,v in genC.items():
	diffMap[k] = (len(genH[k]) - len(genC[k]))
	diffArr.append((len(genH[k]) - len(genC[k])))

import numpy as N
import matplotlib.pyplot as P
from math import sqrt

P.hist(diffArr, bins = 100)
P.show()

arr = diffArr
meanx = N.mean(arr)
n = len(arr)
sumArr = 0
for i in range(1,n):
	sumArr += N.power(arr[i]-meanx,2)
sigma = sqrt(sumArr/n)	
thri_plus = meanx + 2*sigma
thri_min = meanx - 2*sigma

print(thri_plus)
print(thri_min)
f2=open('D://projects/maxThrNew.txt', 'w+')
f3=open('D://projects/minThrNew.txt', 'w+')
for k,v in diffMap.items():
	if v>thri_plus:
		print(k, '\t', v, file=f2)
	if v<thri_plus:
		print(k, '\t', v, file=f3)	





'''

genio = {} #{name: [in, out]}
for k,v in genArr.items():
	bol = False
	if k not in genio:
		genio[k] = [0,1]
		bol = True
	for i in v:
		ki = ''
		for j in i.keys():
			ki = j
		if ki not in genio:
			genio[ki] = [1,0]
	if bol:
		continue
	
	genio[k][1]+=len(v)
	for i in v:
		ki = ''
		for j in i.keys():
			ki = j
		genio[ki][0]+=1
'''		