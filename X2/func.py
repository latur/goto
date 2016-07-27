KISL={
'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAT':'N', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AGA':'R', 'AGC':'S', 'AGG':'R', 'AGT':'S', 'ATA':'I', 'ATC':'I', 'ATG':'M', 'ATT':'I',
'CAA':'Q', 'CAC':'H', 'CAG':'Q', 'CAT':'H', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'GAA':'E', 'GAC':'D', 'GAG':'E', 'GAT':'D', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'TAA':'.', 'TAC':'Y', 'TAG':'.', 'TAT':'Y', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TGA':'.', 'TGC':'C', 'TGG':'W', 'TGT':'C', 'TTA':'L', 'TTC':'F', 'TTG':'L', 'TTT':'F'
,'':'','NNN':'N','TCN':'N','NNA':'N','GCN':'N','ACN':'N','CNN':'N','NAC':'N','NAT':'N','NAA':'N'}
def komp(dnk):
    def io(reed):
        def t(d):
            if d=='T':
                return 'A'
            if d=='G':
                return 'C'
            if d=='A':
                return 'T'
            if d=='C':
                return 'G'
            return 'N'
        bb=[]
        for x in reed:
            bb.append(t(x))
        return bb
    adnk=[]
    for key in dnk.keys():
        adnk.update({key:io(dnk[key])[::-1]})
    return adnk
def op(s):
    f=open(s,'r')
    a=''
    h={}
    for x in f:
        if x[0]=='>':
            a=x[1:]
            continue
        h.update({a[:-2]:x})
    print(len(h))
    return h  
a=op('reads.fa')
def gc_hist(a,l):
    b=len(a['OK1'])//ll
    c=[]
    for x in range(b):
        c.append(a['OK1'][ll*(x-1):ll*x])
    l=[]
    for x in c:
        l.append(x.count('G')+x.count('C'))
    import matplotlib.pyplot as mpl
    print(l)
    mpl.hist(l)
    mpl.show()
def to_amin(reed):
    f=[]
    for trip in range(len(reed)//3):
        f.append(KISL[reed[(trip-1)*3:trip*3]])
    return f

base=[]
to_amin(a['OK1'])
for ok in a:
    base.append(to_amin(a[ok][2:]))
print(len(base))
def to_norm_amin(reeds):
    norm_amin=reeds[0]
    for amin in range(0,len(reeds[0])):
        d_amin=reeds[0][amin]
        for reed in reeds:
            if reed[amin]!=d_amin:
                norm_amin[amin]='#'
    return norm_amin
f=open('test.txt', 'a')
f.write((''.join(to_norm_amin(base))+'\n'))
f.close()






    
    
