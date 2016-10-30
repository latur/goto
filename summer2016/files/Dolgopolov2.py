triplets = {
 "TTT" : "F", "TTC" : "F",
 "TTA" : "L", "TTG" : "L", "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L",
 "ATT" : "I", "ATC" : "I", "ATA" : "I",
 "ATG" : "M",
 "GTT" : "V", "GTC" : "V", "GTA" : "V", "GTG" : "V",
 "TCT" : "S", "TCC" : "S", "TCA" : "S", "TCG" : "S",
 "CCT" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P",
 "ACT" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T",
 "GCT" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A",
 "TAT" : "Y", "TAC" : "Y",
 "TAA" : "J",#Ochra
 "TAG" : "B",#Yantar
 "CAT" : "H", "CAC" : "H",
 "CAA" : "Q", "CAG" : "Q",
 "AAT" : "N", "AAC" : "N",
 "AAA" : "K", "AAG" : "K",
 "GAT" : "D", "GAC" : "D",
 "GAA" : "E", "GAG" : "E",
 "TGT" : "C", "TGC" : "C",
 "TGA" : "O",#Opal
 "TGG" : "W",
 "CGT" : "R", "CGC" : "R",  "CGA" : "R",  "CGG" : "R", "AGA" : "R", "AGG" : "R",
 "AGT" : "S", "AGC" : "S",
 "GGT" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G"
}

a = open("../data/X2/reads.fa")
line = a.read()
a.seek(0)
strs = line.split("\n")
strs.pop()
strs = strs[1::2]


#  Получаю обратные строки 

reversed_strs = []

for s in range(1, len(strs)):
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

 reversed_strs.append(''.join(changed)[::-1])

ideal = ["a" for w in range(len(strs[0]))]

max_letters = []

for i in range(len(strs[0])):
 max_letter_dict = {}
 for j in range(len(strs)):
  if strs[j][i] in max_letter_dict:
   max_letter_dict[strs[j][i]] += 1
  else:
   max_letter_dict[strs[j][i]] = 1

 # print (max_letter_dict)
 max_letter = ('a', 0)
 for k,v in max_letter_dict.items():
  if v > max_letter[1]:
   max_letter = (k,v)
 
 max_letters.append(max_letter_dict)
 ideal[i] = max_letter[0]

ideal = ''.join(ideal)

# print('\n', ideal)

def get_acid_str(s):
 res = ''
 for i in range(0, len(s)-2, 3):
  if not 'N' in s[i:i+3]:
   res += triplets[ s[i:i+3] ]
  else:
   res += 'n'
 return res


# print('N\n\n\n\n\n')
# print(get_acid_str(ideal))

strs_acids = [[],[],[]]
for i in range(3):
 for s in reversed_strs:
  strs_acids[i].append(get_acid_str(s[i:]))

# print(reversed_strs)
# print(strs_acids)

ideal = ['','','']
max_letters = [[],[],[]]

for c in range(3):
 for i in range(len(strs_acids[c][0])):
  max_letter_dict = {}
  for j in range(len(strs_acids[c])):
   if strs_acids[c][j][i] in max_letter_dict:
    max_letter_dict[strs_acids[c][j][i]] += 1
   else:
    max_letter_dict[strs_acids[c][j][i]] = 1 

  # print (max_letter_dict)
  max_letter = ['a', 0, False]
  #last False is for @not mutated
  for k,v in max_letter_dict.items():
   if v > max_letter[1]:
    max_letter = [k,v, False]
  if len(max_letter_dict) > 1:
   max_letter[2] = True


  max_letters[c].append((max_letter_dict, max_letter[2]))
  ideal[c] += max_letter[0]

# print('\n\n\n\n\nLAAAL\n')
print(ideal)

k = 4

exon_array = [] # coordinates (start, end)

j = 0

# print(ideal[0][0])

for i in range(3):
 for letter in range(len(ideal[i][0])):
  # print(max_letters[i])
  if not max_letters[i][letter][1]: #if not mutable
   print("la")
   j += 1
  else:
   if j >= 4:
    exon_array.append(3*(letter - j) + i, 3*letter + i)
   j = 0

print(exon_array)






