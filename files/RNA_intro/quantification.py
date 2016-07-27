__author__ = 'Ira'

import time

start = time.time()

inpfileH = '/Users/Ira/Documents/AU/Research/camp/intro/data/PolyplusH1.22chr.sorted.sam'
inpfileN = '/Users/Ira/Documents/AU/Research/camp/intro/data/PolyplusN1.22chr.sorted.sam'

annfile = '/Users/Ira/Documents/AU/Research/camp/intro/data/Homo_sapiens.38.22chr.genes.gtf'


def count_reads(inpfile, state, genes, genes_start):
    state += 6
    cur_gene_i = 0
    cur_gene_start = genes_start[cur_gene_i]
    with open(inpfile) as inp:
        for line in inp:
            l = line.strip().split()
            flag = int(l[1])
            start = int(l[3])
            end = start + len(l[9]) - 1
            if flag & 16:
                strand = '-'
            else:
                strand = '+'

            #quality check
            if flag & 4:
                continue

            # check position
            if end <= cur_gene_start:
                continue
            if start <= genes[cur_gene_start][1] and strand == genes[cur_gene_start][2]:
                genes[cur_gene_start][state] += 1
            else:
                if start > genes[cur_gene_start][1]:
                    cur_gene_i += 1
                    if cur_gene_i >= len(genes_start):
                        break
                    cur_gene_start = genes_start[cur_gene_i]
                    if end > genes_start[cur_gene_i] and strand == genes[cur_gene_start][2]:
                        genes[cur_gene_start][state] += 1
                elif end > genes_start[cur_gene_i + 1]:
                    genes[genes_start[cur_gene_i + 1]][state] += 1
    sumc = 0
    for gene_st in genes:
        sumc += genes[gene_st][state]
    print sumc

# read annotation
genes_start = []
genes = {}

# genes: key - start, [start, end, strand, id, symbol, function, Ncount, Hcount]
with open(annfile) as inp:
    for line in inp:
        l = line.strip().split('\t')
        genes_start.append(int(l[3]))
        info = l[8].strip(';').split('; ')
        genes[int(l[3])] = [int(l[3]), int(l[4]), l[6], info[0].split(' ')[1].strip('\"'), info[2].split(' ')[1].strip('\"'),
                            info[4].split(' ')[1].strip('\"'), 0, 0]


count_reads(inpfileN, 0, genes, genes_start)  # Norm 0-6

print time.time() - start


count_reads(inpfileH, 1, genes, genes_start)  # Hypo 1-7


diffexpr_up = {}
diffexpr_down = {}
for st in genes:
    norm = genes[st][6]
    hypo = genes[st][7]
    if norm < 10 and hypo < 10:
        continue
    if float(norm)/float(hypo) > 1.5:
        diffexpr_down[genes[st][4]] = float(norm)/float(hypo)
    if float(hypo)/float(norm) > 1.5:
        diffexpr_up[genes[st][4]] = float(hypo)/float(norm)

print len(diffexpr_down)
for i in diffexpr_down:
    print i

print len(diffexpr_up)
for i in diffexpr_up:
    print i








