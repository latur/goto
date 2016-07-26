f=('otv.txt','wr')

def gc(s):
    a=s.upper().count('G')
    a+=s.upper().count('C')
    #print(a/len(s))
    if a/len(s) <0.333:
        return 'E\n'
    if a/len(s)> 0.40:
        return 'E\n'
    return 'C\n'
g=open('test.fa','r')
o=''
for h in g:
    if h[0]=='>':
        continue
    o+=gc(h)
f=open('otv.txt','w')
f.write(o)
f.close()
        
