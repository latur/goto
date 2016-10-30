f=open('D://projects/Homo_sapiens.gtf')
f1=open('C://PolyplusH1.22chr.sorted.sam')
f2=open('C://PolyplusN1.22chr.sorted.sam')
e = []
i1 = -1
while True:
	i1+=1
	line = f.readline()
	if(line == ''):
		break
	e1 = line.split('\t')
	e1 = [e1[3], e1[4], e1[6], e1[8]]
	e.append(e1)
	q = e[i1][3].split('; ')
	str1 = q[2]
	str2 = str1[11:len(q[2])-1]
	e[i1][3] = str2
	#print(e[i1])
saH = []
nowGTFreadH = 0
karH = {} #{name:count}
saN = []
nowGTFreadN = 0
karN = {} #{name:count}
while(True):
	line = f1.readline()
	if(line == ''):
		break
	sa1 = line.split('\t')
	saH = [sa1[1], sa1[3], sa1[8] + sa1[9]]
	saH[2] = int(saH[1]) + len(saH[2]) - 1
	saH[0] = int(saH[0]) & 16
	saH[0] = '-' if saH[0] == 16 else '+'
	for i in range(nowGTFreadH, len(e)):
		if not e[i][2] == saH[0]:
			continue
		elif int(e[i][0])<=int(saH[1]) or int(e[i][1])>=int(saH[2]):
			if e[i][3] in karH:
				karH[e[i][3]]+=1
			else:
				karH[e[i][3]] = 1
			nowGTFreadH = i	
			break

while(True):
	line = f2.readline()
	if(line == ''):
		break
	sa1 = line.split('\t')
	saN = [sa1[1], sa1[3], sa1[8] + sa1[9]]
	saN[2] = int(saN[1]) + len(saN[2]) - 1
	saN[0] = int(saN[0]) & 16
	saN[0] = '-' if saN[0] == 16 else '+'
	for i in range(nowGTFreadN, len(e)):
		if not e[i][2] == saN[0]:
			continue
		elif int(e[i][0])<=int(saN[1]) or int(e[i][1])>=int(saN[2]):
			if e[i][3] in karN:
				karN[e[i][3]]+=1
			else:
				karN[e[i][3]] = 1
			nowGTFreadN = i	
			break	





'''
#print(kar)	
summVH = 0
for k,v in karH.items():
	summVH += v
summVN = 0
for k,v in karN.items():
	summVN += v	
print(len(karH))
print(len(karN))
'''
karE = {}
for k,v in karH.items():
	if karH[k]+karN[k] < 15:
		continue
	karH[k]+=1
	karN[k]+=1
	if karH[k]>karN[k]:
		karE[k] = karH[k] / karN[k]
	else: 
		karE[k] = karN[k] / karH[k]	
keys = karE.keys()
val = karE.values()

##############
for i in range(len(karE)):
        for j in range(len(karE) - 1, i, -1):
            if val[j] < val[j-1]:
            	val[j], val[j-1] = val[j-1], val[j]
                keys[j], keys[j-1] = keys[j-1], keys[j]
##############
karQ
for i in range(len(karE)):
	karQ[keys[i]] = val[i]

print(karQ)

	
		


