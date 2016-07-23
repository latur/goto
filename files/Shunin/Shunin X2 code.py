
# def transform_gene_into_amino(k):
#     aminos = []
#     for gene in genesdict:
#         amino_line = ''
#         for x in range(k, len(genesdict[gene])-2, 3):
#             triplet = genesdict[gene][x]+ genesdict[gene][x+1] + genesdict[gene][x+2]
#             if 'N' in triplet: continue
#             amino_line+=gencode[triplet]
#             #a[x%2]+=gencode[triplet]
#         aminos.append(amino_line)
#     return aminos

# a1 = transform_gene_into_amino(0)
# a2 = transform_gene_into_amino(1)
# a3 = transform_gene_into_amino(2)
# # a = []
# # for gene in genesdict:
# #     a.append(transform_gene_into_amino(genesdict[gene]))
# # print(a[:3])



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


genesdict = form_genesdict('C://Users/Tima/Documents/GitHub/goto/data/X2/reads.fa')

gencode = {'TAT': 'Y', 'TAG': 'X', 'CAA': 'Q', 'CTC': 'L', 'TCG': 'S', 'GGT': 'G', 'CAG': 'Q', 'GGC': 'G', 'TTA': 'L', 'CTA': 'L', 'TTC': 'F', 'CGC': 'R', 'TAA': 'X', 'GCT': 'A', 'GAG': 'E', 'GAA': 'E', 'AGT': 'S', 'AAA': 'K', 'TGT': 'C', 'CGG': 'R', 'GTG': 'V', 'ACA': 'T', 'TCT': 'S', 'AGG': 'R', 'CAT': 'H', 'CCT': 'P', 'ATC': 'I', 'ACT': 'T', 'AAT': 'N', 'ACG': 'T', 'GGA': 'G', 'GTT': 'V', 'TCA': 'S', 'GGG': 'G', 'CGA': 'R', 'TCC': 'S', 'GAT': 'D', 'CCA': 'P', 'AAG': 'K', 'AGA': 'R', 'GCA': 'A', 'GCC': 'A', 'CAC': 'H', 'CTG': 'L', 'CTT': 'L', 'TGA': 'X', 'TAC': 'Y', 'TGG': 'W', 'GCG': 'A', 'ATG': 'M', 'CCC': 'P', 'ATA': 'I', 'CCG': 'P', 'ATT': 'I', 'AGC': 'S', 'TTT': 'F', 'CGT': 'R', 'GAC': 'D', 'ACC': 'T', 'TTG': 'L', 'TGC': 'C', 'GTC': 'V', 'AAC': 'N', 'GTA': 'V'}


def complement_dna(dna):
    result_dna = ''
    for nuc in dna:
        if nuc == 'T':
            result_dna+='A'
        elif nuc == 'A':
            result_dna+='T'
        elif nuc == 'G':
            result_dna+='C'
        elif nuc == 'C':
            result_dna+='G'
    #result_dna = ''.join(reversed(result_dna))
    return result_dna[::-1]

# def find_mutation(column):
#     pass

# def form_columns(genesdict):
#     columns = []
#     for gene in genesdict:
#         for x in range(len(genesdict[gene])-2):
#             columns.append([])
#         break            
#     for gene in genesdict:
#         for x in range(len(genesdict[gene])-2):
#             triplet = genesdict[gene][x] + genesdict[gene][x+1] + genesdict[gene][x+2] 
#             if 'N' in triplet: continue
#             amino = gencode[triplet]
#             columns[x].append(amino)
#     return columns


# columns = form_columns(genesdict)

# mutations = []
# for column in range(0, len(columns), 3):
#     if len(set(columns[column])) > 1:
#         mutations.append(' ')
#     elif len(set(columns[column])) == 1:
#         mutations.append(columns[column][0])

# resfile = open('C://Users/Tima/Desktop/resfile1.txt', 'w')
# print(''.join(mutations), file=resfile)
# resfile.close()



def form_complement_genesdict(genesdict):
    complement_genesdict = genesdict
    for x in complement_genesdict:
        complement_genesdict[x] = complement_dna(genesdict[x])
    return complement_genesdict


def translate(gene, k):
    aminos = ''
    for x in range(k, len(gene)-2, 3):
        triplet = gene[x:x+3]
        if 'N' in triplet:aminos+=' '; continue
        aminos+=gencode[triplet]
    return aminos

def translate_all(genesdict, k):
    aminos_list = []
    for gene in genesdict.values():
        aminos_list.append(translate(gene, k))
    return aminos_list


def transform_aminos_list(aminos_list):
    aminos_column = []
    for x in aminos_list[0]:
        aminos_column.append([])
    for amino in aminos_list:
        for x in range(len(amino)):
            aminos_column[x].append(amino[x])
    return aminos_column
#print(transform_aminos_list(['23', '24', '17', '17']))

def find_mutations(aminos_column):
    mutations = ''
    for aminos in aminos_column:
        if len(set(aminos))>1:
            mutations+=' '
        else:
            mutations+=aminos[0]
    return mutations

def reverse_mutations(mutations):
    return mutations[::-1]

a = []

def get_random_nucline(genesdict):
    for gene in genesdict:
        return genesdict[gene]


def find_exons(mutations_line, min_length, k):
    exons = []
    #exons_in_amino = []
    ml = mutations_line[:]
    probable_exons = sorted(ml.split())
    for exon in probable_exons:
        #if 'X' in exon:continue
        if len(exon) >= min_length:
            exons.append(str(mutations_line.index(exon)*3-k) +'\t' + str((mutations_line.index(exon)+len(exon))*3-k))
            #exons_in_amino.append(mutations_line[mutations_line.index(exon):mutations_line.index(exon)+len(exon)])
    return exons#, exons_in_amino

def write_to_file(min_length, complement):
    if not complement:
        resfile = open('C://Users/Tima/Desktop/biology/files/resfile0.txt', 'w')
        nucline = get_random_nucline(genesdict)
        for x in range(3):
            for y in find_exons(find_mutations(transform_aminos_list(translate_all(genesdict, x))), min_length,x):
               print(y, file=resfile)

    #print(a)
    else:
        resfile = open('C://Users/Tima/Desktop/biology/files/resfile1.txt', 'w')
        nucline = get_random_nucline(form_complement_genesdict(genesdict))
        for x in range(3):
            for y in find_exons(reverse_mutations(find_mutations(transform_aminos_list(translate_all(form_complement_genesdict(genesdict), x)))), min_length,x):
                print(y, file=resfile)
    resfile.close()


write_to_file(2, False)
# for x in range(3):
#     #a.append(find_exons(find_mutations(transform_aminos_list(translate_all(genesdict, x))), 9,x))
#     a.append(find_exons(reverse_mutations(find_mutations(transform_aminos_list(translate_all(form_complement_genesdict(genesdict), x)))), 9,x))

# def form_slices_from_exons(exons):
#     slice_list = []
#     for exon in exons:
#         for x in exon:
#             slice_list.append(x)
#     len_dict = {}
#     for x in slice_list:
#         if len(x) in len_dict:
#             len_dict[len(x)].append(x)
#         else:
#             len_dict[len(x)] = []
#             len_dict[len(x)].append(x)    
#     slice_list = []
#     for x in sorted(len_dict.keys(), reverse=True):
#         for y in sorted(len_dict[x], reverse=True):
#             #print(slice(int(y.split('\t')[1]), int(y.split('\t')[1])))
#             slice_list.append(slice(int(y.split('\t')[0]), int(y.split('\t')[1])))
#     #print(slice_list)
#     return slice_list
# b = ''
# line = get_random_nucline(form_complement_genesdict(genesdict))
# #print(line[:100])01
# for x in form_slices_from_exons(a):
#     #print(line[slice(857)])
#     b+=line[x]

# print(translate(b, 0))

