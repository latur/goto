from collections import Counter

KISL={
'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I',
'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'TAA':'.', 'TAC':'Y', 'TAG':'.', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TGA':'.', 'TGC':'C', 'TGG':'W', 'TGT':'C', 'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F'
,'':''}
def komp(dnk):
    def t(f):
        if d=='T':
            return 'A'
        if d=='G':
            return 'C'
        if d=='A':
            return 'T'
        if d=='C':
            return 'G'
        return ''
    k=''
    if dnk=='':
        return ''
    for i in dnk:
        k+=t(i)
    


f= open('/home/krtk/git1/goto/X1/train.fa', 'r')
c={}
e={}
c_gc=[]
e_gc=[]
p='f'
for line in f:

    if line[0]=='>':
        if line[:2]=='>C':
            
            p=line[1:]
        if line[:2]=='>E':
            
            p=line[1:]
    else:
        if p[0]=='C':
            c.update({p:line})
        else:
            e.update({p:line})
ccl=0
el=0
c_gc2=[]
e_gc2=[]
for i in e.values():
    el+=len(i)
    if i.lower().find('g')!= -1:
        e_gc.append(i.lower().count('c')/len(i))
    else: 
        e_gc.append(i.lower().count('g')/len(i))
for i in c.values():
    ccl+=len(i)
    if i.lower().find('g')!= -1:
        c_gc.append(i.lower().count('c')/len(i))
    else: 
        c_gc.append(i.lower().count('g')/len(i))
print(ccl)
print(el)
'''
for i in c_gc:
    c_gc2.append(i/ccl)    
for i in e_gc:
    e_gc2.append(i/el)''' 
import matplotlib.pyplot as mpl
print(len(e_gc),len(c_gc))
mpl.hist(c_gc)
mpl.hist(e_gc)
mpl.show()
'''g=Counter()
f=[]       
for p in e.values():
    f=[]
    for  i in range(len(p)//3):
        f.append(p[(i-1)*3:i*3])
    for word in f:
        g[KISL[word.upper()]]+=1
print(g)
l=g
g=Counter()
#------------------------
for p in c.values():
    f=[]
    for  i in range(len(p)//3):
        f.append(p[(i-1)*3:i*3])
    for word in f:
        
        g[KISL[word.upper()]]+=1
print(l-g)'''
