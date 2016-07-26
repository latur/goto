import random
f=open('test.txt')
o=''
for s in f:
    o=''
    j=0
    c=''
    for  b in range(0,len(s)):
        
        
        if s[b]=='#':
            if len(c)<3:
                c=''
                j=b+1
            else:
                
                o+=str(j*3)+ '\t'+str(b*3)+'\n'
                j=b+1
                c=''

        else:
            c+=s[b]
            if s[b]=='N':
                c=''
                j=b+1
    v=open('r1'+str(random.randint(1,999))+'.txt','w')
    v.write(o)
    v.close()

       
            
            
        
