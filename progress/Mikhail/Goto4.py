f=open('D://projects/HumanNet.txt')
genArr = {}  #{nach: [ {}, {}, {} ] }
while True:
	line = f.readline()
	if line == "":
		break
	lineAr = line.strip().split(' ')
	lineAr[2] = float(lineAr[2])
	reb = {}
	reb[lineAr[1]] = lineAr[2]
	if lineAr[0] not in genArr:
		genArr[lineAr[0]] = []
	genArr[lineAr[0]].append(reb)
#print(genArr)

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


import numpy as N
import matplotlib.pyplot as P
from math import sqrt
iArr = []
oArr = []
for k,v in genio.items():
	iArr.append(v[0])
	oArr.append(v[1])
#P.hist(iArr, bins = 100)
#P.show()
arr = iArr
meanx = N.mean(arr)
n = len(arr)
sumArr = 0
for i in range(1,n):
	sumArr += N.power(arr[i]-meanx,2)
sigma = sqrt(sumArr/n)	
thri = meanx+ 2*sigma

arr = oArr
meanx = N.mean(arr)
n = len(arr)
sumArr = 0
for i in range(1,n):
	sumArr += N.power(arr[i]-meanx,2)
sigma = sqrt(sumArr/n)	
thro = meanx+ 2*sigma

oGen = []
for k,v in genio.items():
	if float(v[1]) > thro:
		oGen.append(k)

print(oGen)			