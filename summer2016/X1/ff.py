def prob1():
    from collections import Counter, OrderedDict
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
    d=Counter()
    a=Counter()
    def mmo(r,c):
        
        for i in range(len(r)-4):
            
            d[r[i-1:i+3]]+=1
        return d
    for i in c.values():
        a+=mmo(i,d)
    sl={}
    a=OrderedDict(a)
    d=Counter()
    for u in a:
        d[u[:3]]+=a[u]

    for u in a:
        a[u]=a[u]/d[u[:3]]
    print(a)


def prob2():
    from collections import Counter, OrderedDict
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
    d=Counter()
    a=Counter()
    def mmo(r,c):
        
        for i in range(len(r)-4):
            
            d[r[i-1:i+3]]+=1
        return d
    for i in e.values():
        a+=mmo(i,d)
    sl={}
    a=OrderedDict(a)
    d=Counter()
    for u in a:
        d[u[:3]]+=a[u]

    for u in a:
        a[u]=a[u]/d[u[:3]]
    print(a)
for reeds in c:
    mmo(c[reeds],a)
print(a)
