f=open('D://projects/files/NewHumanNet.txt')
f1=open('D://projects/files/Cancer_LUAD_Network.txt')
genArrH = [] #{ out: [ in ] }
genArrC = [] #{ out: [ {in:expr}, ... ] }
genArrHrev = []
for  line in f:
	if line == "":
		break
	lineAr = line.strip().split('\t')
	line = lineAr[0] + lineAr[1]
	linerev = lineAr[1] + lineAr[0]
	genArrH.append(line)
	genArrHrev.append(linerev)

print(0)
for line in f1:
	if line == "":
		break
	lineAr = line.strip().split('\t')
	line = lineAr[0] + lineAr[1]	
	genArrC.append(line)
print(1)
print(len(genArrH))
diffC = []
for i in genArrC:
	#print(i)
	if i not in genArrH or i not in genArrHrev:
		diffC.append(i)
print(2)
diffCrez = len(diffC) / len(genArrC)
print(diffCrez)		