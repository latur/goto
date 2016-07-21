# file = open('C://Users/Tima/Documents/GitHub/goto/X1/train.fa', 'r')
# a = file.readlines()
# file.close()
# genesdict = {}
# for x in range(len(a)-1):
#     if x%2==0:
#         name = a[x].replace('>','').replace('\n','')
#         data = a[x+1].replace('\n','')
#         genesdict[name] = data

# gistE = {}
# for x in range(101):
#     gistE[x] = 0

# gistC = {}
# for x in range(101):
#     gistC[x] = 0



# def count_gist():   
#     for x in genesdict:
#         if x[0] == 'E':
#             gistE[find_gc(genesdict[x])]+=1
#         if x[0] == 'C':
#             gistC[find_gc(genesdict[x])]+=1   


# count_gist()

# resfile = open('C://Users/Tima/Desktop/refile.txt', 'w')
# print('Гистограмма для C', file=resfile)
# print(gistC, file=resfile)
# print('\n\n', file=resfile)
# print('Гистограмма для E', file=resfile)
# print(gistE, file=resfile)
# resfile.close()
























from math import log


file = open('C://Users/Tima/Documents/GitHub/goto/X1/train.fa', 'r')
a = file.readlines()
file.close()



genesdict = {}
for x in range(len(a)-1):
    if x%2==0:
        name = a[x].replace('>','').replace('\n','')
        data = a[x+1].replace('\n','')
        genesdict[name] = data

gencode = {'TAT': 'Y', 'TAG': 'X', 'CAA': 'Q', 'CTC': 'L', 'TCG': 'S', 'GGT': 'G', 'CAG': 'Q', 'GGC': 'G', 'TTA': 'L', 'CTA': 'L', 'TTC': 'F', 'CGC': 'R', 'TAA': 'X', 'GCT': 'A', 'GAG': 'E', 'GAA': 'E', 'AGT': 'S', 'AAA': 'K', 'TGT': 'C', 'CGG': 'R', 'GTG': 'V', 'ACA': 'T', 'TCT': 'S', 'AGG': 'R', 'CAT': 'H', 'CCT': 'P', 'ATC': 'I', 'ACT': 'T', 'AAT': 'N', 'ACG': 'T', 'GGA': 'G', 'GTT': 'V', 'TCA': 'S', 'GGG': 'G', 'CGA': 'R', 'TCC': 'S', 'GAT': 'D', 'CCA': 'P', 'AAG': 'K', 'AGA': 'R', 'GCA': 'A', 'GCC': 'A', 'CAC': 'H', 'CTG': 'L', 'CTT': 'L', 'TGA': 'X', 'TAC': 'Y', 'TGG': 'W', 'GCG': 'A', 'ATG': 'M', 'CCC': 'P', 'ATA': 'I', 'CCG': 'P', 'ATT': 'I', 'AGC': 'S', 'TTT': 'F', 'CGT': 'R', 'GAC': 'D', 'ACC': 'T', 'TTG': 'L', 'TGC': 'C', 'GTC': 'V', 'AAC': 'N', 'GTA': 'V'}

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
            result_dna+='A'
        elif x == 'A':
            result_dna+='T'
        elif x == 'G':
            result_dna+='C'
        elif x == 'C':
            result_dna+='G'
    #result_dna = ''.join(reversed(result_dna))
    return result_dna[::-1]

# def find_aminos_in_gene(gene):
#     aminos = {'V': 0, 'Y': 0, 'C': 0, 'T': 0, 'L': 0, 'E': 0, 'D': 0, 'N': 0, 'I': 0, 'M': 0, 'P': 0, 'S': 0, 'H': 0, 'X': 0, 'Q': 0, 'G': 0, 'F': 0, 'A': 0, 'K': 0, 'W': 0, 'R': 0}
#     complement_dna = complement(gene)
#     for x in range(len(gene)-2):
#         triplet = gene[x]+gene[x+1]+gene[x+2]
#         aminos[gencode[triplet]]+=1
#     for x in range(len(complement_dna)-2):
#         triplet = gene[x]+gene[x+1]+gene[x+2]
#         aminos[gencode[triplet]]+=1
#     return aminos

# def definer(aminos, percent):
#     percent = 0
#     if aminos['A'] > 67:
#         percent+=5
#     if aminos['C'] < 51:
#         percent+=5
#     if aminos['E'] < 69:
#         percent+=5
#     if aminos['D'] < 44:
#         percent+=5
#     if aminos['G'] > 76:
#         percent+=5
#     if aminos['F'] > 172:
#         percent+=5
#     if aminos['I'] < 132:
#         percent+=5
#     if aminos['H'] < 47:
#         percent+=5
#     if aminos['K'] < 150:
#         percent+=5
#     if aminos['M'] < 27:
#         percent+=5
#     if aminos['L'] < 178:
#         percent+=5
#     if aminos['N'] < 102:
#         percent+=5
#     if aminos['Q'] < 63:
#         percent+=5
#     if aminos['P'] > 68:
#         percent+=5
#     if aminos['S'] < 159:
#         percent+=5
#     if aminos['R'] > 114:
#         percent+=5
#     if aminos['T'] < 87:
#         percent+=5
#     if aminos['W'] < 23:
#         percent+=5
#     if aminos['V'] < 87:
#         percent+=5
#     if aminos['Y'] < 53:
#         percent+=5
#     if percent>90:
#         return 'E'
#     else:
#         return 'C'


# def define_read(gene):
#     gc = find_gc(gene)
#     if 29<gc<45:
#         return definer(find_aminos_in_gene(gene), 30)
#     else:
#         return definer(find_aminos_in_gene(gene), -5)

# result = ''

# for x in genesdict:
#     result+= define_read(genesdict[x]) + ' '

# resfile = open('C://Users/Tima/Desktop/refile.txt', 'w')
# print(result, file=resfile)
# resfile.close()



def form_genesdict(filepath):
    file = open(filepath, 'r')
    filelines = file.readlines()
    file.close()
    genesdict = {}
    for line_number in range(len(filelines)-1):
        if line_number%2==0:
            name = filelines[line_number].replace('>','').replace('\n','')
            data = filelines[line_number+1].replace('\n','')
            genesdict[name] = data
    return genesdict


def add_nuc_to_chain(chain):
    nuc = ['T', 'G', 'C', 'A']
    result_chain = {}
    for x in chain:
        for y in nuc:
            result_chain[x+y]=1
    return result_chain

def gen_base_markchain(k):
    nuc = ['T', 'G', 'C', 'A']
    if k <= 1:
        return {'T':1, 'G':1, 'C':1, 'A':1}
    else:
        return add_nuc_to_chain(gen_base_markchain(k-1))


def find_n_plets(k, gene, markchain):
    for x in range(len(gene)-k):
            n_plet = ''
            for i in range(k):
                n_plet+=gene[x+i]
            markchain[n_plet]+=1
    return markchain

def form_markchain(k, read_dict, type):
    markchain = gen_base_markchain(k)
    lower_markchain = gen_base_markchain(k-1)
    genes = []
    for x in read_dict:
        if x[0] == type:
            genes.append(read_dict[x])
    for gene in genes:
        markchain = find_n_plets(k, gene, markchain)
        lower_markchain = find_n_plets(k-1, gene, lower_markchain)
    for n_plet in markchain:
        markchain[n_plet] = markchain[n_plet]/lower_markchain[n_plet[:len(n_plet)-1]]
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
    return('[' + str(e_probability) + ',' + str(c_probability) + ']\n')
    # if e_probability>c_probability:
    #     return 'E '
    # else:
    #     return 'C '

train_genesdict = form_genesdict('C://Users/Tima/Documents/GitHub/goto/X1/train.fa')
test_genesdict  = form_genesdict('C://Users/Tima/Documents/GitHub/goto/X1/test.fa')
E_chain = form_markchain(8, train_genesdict, 'E')
C_chain = form_markchain(8, train_genesdict, 'C')


result = ''
for gene in test_genesdict:
    result+=find_probability(8, E_chain, C_chain, test_genesdict[gene])
resfile = open('C://Users/Tima/Desktop/resfile.txt', 'w')
print(result, file=resfile)
resfile.close()
