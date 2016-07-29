f = open('NewHumanNet.txt')
f1 = open('Cancer_LUAD_Network.txt')

genArrH = []  # { out: [ in ] }
genArrC = []  # { out: [ {in:expr}, ... ] }

for line in f:
    lineAr = line.strip().split('\t')
    line = lineAr[0] + lineAr[1]
    linerev = lineAr[1] + lineAr[0]
    genArrH.append(line)
    genArrH.append(linerev)

print(0)

for line in f1:
    lineAr = line.strip().split('\t')
    line = lineAr[0] + lineAr[1]
    if line in genArrH:
        genArrC.append(line)
        print len(genArrC)

print len(genArrC)
# print(1)
# print(len(genArrH))
# diffC = []
# for i in genArrC:
#     # print(i)
#     if i not in genArrH or i not in genArrHrev:
#         diffC.append(i)
# print(2)
# diffCrez = len(diffC) / len(genArrC)
# print(diffCrez)
f.close()
f1.close()