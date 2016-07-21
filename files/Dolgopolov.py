triplets = {
 "TTT" : "F",
 "TTC" : "F",
 "TTA" : "L",
 "TTG" : "L",
 "CTT" : "L",
 "CTC" : "L",
 "CTA" : "L",
 "CTG" : "L",
 "ATT" : "I",
 "ATC" : "I",
 "ATA" : "I",
 "ATG" : "M",
 "GTT" : "V",
 "GTC" : "V",
 "GTA" : "V",
 "GTG" : "V",
 "TCT" : "S",
 "TCC" : "S",
 "TCA" : "S",
 "TCG" : "S",
 "CCT" : "P",
 "CCC" : "P",
 "CCA" : "P",
 "CCG" : "P",
 "ACT" : "T",
 "ACC" : "T",
 "ACA" : "T",
 "ACG" : "T",
 "GCT" : "A",
 "GCC" : "A",
 "GCA" : "A",
 "GCG" : "A",
 "TAT" : "Y",
 "TAC" : "Y",
 "TAA" : "Ochra",
 "TAG" : "Yantar",
 "CAT" : "H",
 "CAC" : "H",
 "CAA" : "Q",
 "CAG" : "Q",
 "AAT" : "N",
 "AAC" : "N",
 "AAA" : "K",
 "AAG" : "K",
 "GAT" : "D",
 "GAC" : "D",
 "GAA" : "E",
 "GAG" : "E",
 "TGT" : "C",
 "TGC" : "C",
 "TGA" : "Opal",
 "TGG" : "W",
 "CGT" : "R",
 "CGC" : "R", 
 "CGA" : "R", 
 "CGG" : "R",
 "AGA" : "R",
 "AGG" : "R",
 "AGT" : "S",
 "AGC" : "S",
 "GGT" : "G",
 "GGC" : "G",
 "GGA" : "G",
 "GGG" : "G"
}

num_of_acids = [{
 "F" : 0,
 "L" : 0,
 "I" : 0,
 "M" : 0,
 "V" : 0,
 "S" : 0,
 "P" : 0,
 "T" : 0,
 "A" : 0,
 "Y" : 0,
 "Ochra" : 0,
 "Yantar" : 0,
 "H" : 0,
 "Q" : 0,
 "N" : 0,
 "K" : 0,
 "D" : 0,
 "E" : 0,
 "C" : 0,
 "Opal" : 0,
 "W" : 0,
 "R" : 0,
 "S" : 0,
 "G" : 0,
} for i in range(2)]


a = open("train.fa")
line = a.read()
a.seek(0)
strs = line.split("\n")
strs.pop()


#  Получаю обратные строки 

reversed_strs = []

for s in range(1, len(strs), 2):
 changed = list(strs[s])
 for i in range(len(changed)):
  if changed[i] == 'A':
   changed[i] = 'T'
  elif changed[i] == 'T':
   changed[i] = 'A'
  elif changed[i] == 'G':
   changed[i] = 'C'
  elif changed[i] == 'C':
   changed[i] = 'G'

 reversed_strs.append((strs[s-1][1], ''.join(changed)[::-1]))

# num of letters in combos
k = 4

nuc = ['T', 'G', 'C', 'A']

def add_nuc_to_chain(chain):
 global nuc
 result_chain = {}
 for i in chain:
  for j in nuc:
   result_chain[i+j]=1
 return result_chain

def gen_base_markchain(k):
 global nuc
 if k <= 1:
  return {'T':1, 'G':1, 'C':1, 'A':1}
 else:
  return add_nuc_to_chain(gen_base_markchain(k-1))

mdict = gen_base_markchain(k)
mdict = [mdict, mdict]

# print(mdict, len(mdict))

for s in range(1, len(strs), 2):
 if strs[s-1][1] == "C":
  for i in range(len(strs[s]) - 3):
   mdict[0][ strs[s][i:i+4] ] += 1

 else:
  for i in range(len(strs[s]) - 3):
   mdict[1][ strs[s][i:i+4] ] += 1

for s in range(len(reversed_strs)):
 if reversed_strs[s][0] == "C":
  for i in range(len(reversed_strs[s][1]) - 3):
   mdict[0][ reversed_strs[s][1][i:i+4] ] += 1

 else:
  for i in range(len(reversed_strs[s][1]) - 3):
   mdict[1][ reversed_strs[s][1][i:i+4] ] += 1

print(mdict)

#one step smaller array
mdict_small = []

#КОСТЫЛИ КОСТЫЛИ
N = k
###
for k,v in gen_base_markchain(N-1).items():
 mdict_small.append(k)


statistics = gen_base_markchain(N)
statistics = [statistics, statistics]
#ATGC
def get_procent_for_nplet():
 global nuc
 global statistics
 for x in range(2):
  for k in mdict_small:
   msum = 0
   for i in nuc:
    msum += mdict[x][k+i]
   for i in nuc:
    statistics[x][k+i] = mdict[x][k+i] / msum

get_procent_for_nplet()

print(statistics)   
  
