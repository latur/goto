gencode = {
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

# num_of_acids = [{
#  "F" : 0,
#  "L" : 0,
#  "I" : 0,
#  "M" : 0,
#  "V" : 0,
#  "S" : 0,
#  "P" : 0,
#  "T" : 0,
#  "A" : 0,
#  "Y" : 0,
#  "Ochra" : 0,
#  "Yantar" : 0,
#  "H" : 0,
#  "Q" : 0,
#  "N" : 0,
#  "K" : 0,
#  "D" : 0,
#  "E" : 0,
#  "C" : 0,
#  "Opal" : 0,
#  "W" : 0,
#  "R" : 0,
#  "S" : 0,
#  "G" : 0,
# } for i in range(2)]

# from math import log

# a = open("../data/X1/train.fa")
# line = a.read()
# a.seek(0)
# a.close()
# strs = line.split("\n")
# strs.pop()


# #  Получаю обратные строки 

# reversed_strs = []

# for s in range(1, len(strs), 2):
#  changed = list(strs[s])
#  for i in range(len(changed)):
#   if changed[i] == 'A':
#    changed[i] = 'T'
#   elif changed[i] == 'T':
#    changed[i] = 'A'
#   elif changed[i] == 'G':
#    changed[i] = 'C'
#   elif changed[i] == 'C':
#    changed[i] = 'G'

#  reversed_strs.append((strs[s-1][1], ''.join(changed)[::-1]))

# # num of letters in combos

# mdict = gen_base_markchain(k)
# mdict = [mdict, mdict]

# # print(mdict, len(mdict))

# for s in range(1, len(strs), 2):
#  if strs[s-1][1] == "C":
#   for i in range(len(strs[s]) - 3):
#    mdict[0][ strs[s][i:i+4] ] += 1

#  else:
#   for i in range(len(strs[s]) - 3):
#    mdict[1][ strs[s][i:i+4] ] += 1

# for s in range(len(reversed_strs)):
#  if reversed_strs[s][0] == "C":
#   for i in range(len(reversed_strs[s][1]) - 3):
#    mdict[0][ reversed_strs[s][1][i:i+4] ] += 1

#  else:
#   for i in range(len(reversed_strs[s][1]) - 3):
#    mdict[1][ reversed_strs[s][1][i:i+4] ] += 1

# print(mdict)

# #one step smaller array
# mdict_small = []

# #КОСТЫЛИ КОСТЫЛИ
# N = k
# ###
# for k,v in gen_base_markchain(N-1).items():
#  mdict_small.append(k)


# statistics = gen_base_markchain(N)
# statistics = [statistics, statistics]
# #ATGC
# def get_procent_for_nplet():
#  global nuc
#  global statistics
#  for x in range(2):
#   for k in mdict_small:
#    msum = 0
#    for i in nuc:
#     msum += mdict[x][k+i]
#    for i in nuc:
#     statistics[x][k+i] = mdict[x][k+i] / msum

# get_procent_for_nplet()

# print(statistics)

# -*- coding: utf-8 -*-

from math import log


file = open('../data/X1/train.fa')
a = file.readlines()
file.close()



genesdict = {}
for x in range(len(a) - 1):
    if x%2 == 0:
        name = a[x].replace('>','').replace('\n','')
        data = a[x+1].replace('\n','')
        genesdict[name] = data

# gencode = {'TAT': 'Y', 'TAG': 'X', 'CAA': 'Q', 'CTC': 'L', 'TCG': 'S', 'GGT': 'G', 'CAG': 'Q', 'GGC': 'G', 'TTA': 'L', 'CTA': 'L', 'TTC': 'F', 'CGC': 'R', 'TAA': 'X', 'GCT': 'A', 'GAG': 'E', 'GAA': 'E', 'AGT': 'S', 'AAA': 'K', 'TGT': 'C', 'CGG': 'R', 'GTG': 'V', 'ACA': 'T', 'TCT': 'S', 'AGG': 'R', 'CAT': 'H', 'CCT': 'P', 'ATC': 'I', 'ACT': 'T', 'AAT': 'N', 'ACG': 'T', 'GGA': 'G', 'GTT': 'V', 'TCA': 'S', 'GGG': 'G', 'CGA': 'R', 'TCC': 'S', 'GAT': 'D', 'CCA': 'P', 'AAG': 'K', 'AGA': 'R', 'GCA': 'A', 'GCC': 'A', 'CAC': 'H', 'CTG': 'L', 'CTT': 'L', 'TGA': 'X', 'TAC': 'Y', 'TGG': 'W', 'GCG': 'A', 'ATG': 'M', 'CCC': 'P', 'ATA': 'I', 'CCG': 'P', 'ATT': 'I', 'AGC': 'S', 'TTT': 'F', 'CGT': 'R', 'GAC': 'D', 'ACC': 'T', 'TTG': 'L', 'TGC': 'C', 'GTC': 'V', 'AAC': 'N', 'GTA': 'V'}

def find_gc(gene):
    gc_count = 0
    for x in gene:
        if x == 'G' or x == 'C':
            gc_count+=1
    return int((gc_count/len(gene))*100)


def complement(dna):
    result_dna = ''
    for x in dna:
        if x == 'T':
            result_dna += 'A'
        elif x == 'A':
            result_dna += 'T'
        elif x == 'G':
            result_dna += 'C'
        elif x == 'C':
            result_dna += 'G'
    #result_dna = ''.join(reversed(result_dna))
    return result_dna[::-1]

def form_genesdict(filepath):
    file = open(filepath, 'r')
    filelines = file.readlines()
    file.close()
    genesdict = {}
    for line_number in range(len(filelines) - 1):
        if line_number%2 == 0:
            name = filelines[line_number].replace('>','').replace('\n','')
            data = filelines[line_number + 1].replace('\n','')
            genesdict[name] = data
    return genesdict


def add_nuc_to_chain(chain):
    nuc = ['T', 'G', 'C', 'A']
    result_chain = {}
    for x in chain:
        for y in nuc:
            result_chain[x + y]=1
    return result_chain

def gen_base_markchain(k):
    nuc = ['T', 'G', 'C', 'A']
    if k <= 1:
        return {'T':1, 'G':1, 'C':1, 'A':1}
    else:
        return add_nuc_to_chain(gen_base_markchain(k - 1))


def find_n_plets(k, gene, markchain):
    for x in range(len(gene) - k):
            n_plet = ''
            for i in range(k):
                n_plet += gene[x + i]
            markchain[n_plet] += 1
    return markchain

def form_markchain(k, read_dict, type):
    markchain = gen_base_markchain(k)
    lower_markchain = gen_base_markchain(k - 1)
    genes = []
    for x in read_dict:
        if x[0] == type:
            genes.append(read_dict[x])
    for gene in genes:
        markchain = find_n_plets(k, gene, markchain)
        lower_markchain = find_n_plets(k - 1, gene, lower_markchain)
    for n_plet in markchain:
        markchain[n_plet] = float(markchain[n_plet]) / lower_markchain[n_plet[:len(n_plet) - 1]]
    return markchain


def find_probability(k, E_chain, C_chain, gene):
    e_probability = 1
    c_probability = 1
    for x in range(len(gene)-k):
        n_plet = ''
        for i in range(k):
            n_plet+=gene[x+i]
        e_probability += log(E_chain[n_plet])
        c_probability += log(C_chain[n_plet])
    # return('[' + str(e_probability) + ',' + str(c_probability) + ']\n')
    if e_probability>c_probability:
        return 'E '
    else:
        return 'C '

train_genesdict = form_genesdict('../data/X1/train.fa')
E_chain = form_markchain(7, train_genesdict, 'E')
C_chain = form_markchain(7, train_genesdict, 'C')

result = ''
f = open('../data/X1/test.fa')
for line in f.readlines():
  if line == '' : continue
  if line[0] == '>' : continue
  xread = line.replace('\n','')
  find_probability(7, E_chain, C_chain, xread)
f.close()

resfile = open('../data/X1/resfile', 'w')
print(result, file=resfile)
resfile.close()