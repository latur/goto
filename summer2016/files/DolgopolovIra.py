f = open('../data/RNA_intro/Homo_sapiens.38.22chr.genes.gtf')
f_sam = open('../../PolyplusN1.22chr.sorted.sam')
gen_info = []
gen_read = []

while True:
 line = f.readline()
 if line != '':
 	pass
  # print(line)
 else: break
 parsed = line.split('\t')
 gen_name = parsed[8].split('; ')[2]
 gen_info.append((int(parsed[3]), int(parsed[4]), True if parsed[6] == '+' else False, gen_name[11:len(gen_name)-1]))
 #start, end, straight/reversed, gene_name
 # print(parsed[6], gen_info[-1][2])
 

# while False:
while True:
 line = f_sam.readline()
 if line == '':
  break
 parsed = line.split('\t')
 gen_read.append((int(parsed[3]), int(parsed[3]) + 50, int(parsed[1])&16 != 16, parsed[9]))
 #beginning, end, straight/reversed, gene_str

f.close()
f_sam.close()

# print(gen_info[0], gen_read[0])
print('просчитано')

res = {}
#res of gen and count

for n, i in enumerate(gen_read):
 # last_plus = 5
 last = 5

 # k = (last_plus if i[2] else last_minus) - 5 
 k = last - 5
 if k < 0: k = 0

 while True:
 	if k >= len(gen_info) or gen_info[k][1] > i[1] + 20:
 		break
 	if gen_info[k][2] == i[2] and \
 	  (gen_info[k][0] > i[0] and gen_info[k][0] < i[1] or \
 				gen_info[k][1] > i[0] and gen_info[k][1] < i[1] or \
 				gen_info[k][0] < i[0] and gen_info[k][1] > i[1]):
 	 if gen_info[k][3] in res:
 	 	res[gen_info[k][3]] += 1
 	 else:
 	 	res[gen_info[k][3]] = 1

 	 # if i[2]:
 	 last = k
 	 # else:
 	 	# last_minus = k
 	 # break
 	k += 1
 if n%10000 == 0: print('len: ', len(res))


summa = 0
for k,v in res.items():
	summa += v
print('sum: ', summa)
