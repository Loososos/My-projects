import random
import itertools

def reject(s):
    if int(s)==0: return str(5)
    if int(s)==1: return str(4)
    if int(s)==2: return str(3)
    if int(s)==3: return str(2)
    if int(s)==4: return str(1)
    if int(s)==5: return str(0)

def beetwen(s,coo):
    T=True
    l=[]
    l.append((s[0],s[1]))
    l.append((reject(s[0]),s[1]))
    l.append((reject(s[0]),reject(s[1])))
    l.append((s[0],reject(s[1])))
    for i in range(len(l)):
        if l[i] in coo: T=False
    return T

def generator():
    coo=[]
    for i in itertools.product('012345',repeat=2):
        coo.append(i)
    g=[]
    i=0
    while i<9:
        a=random.choice(coo)
        if beetwen(a,g)==True:
            g.append(a)
        else: i-=1 
        i+=1
    return g

def cut(s):
    l=[]
    for i in range(6):
        l.append(s[i*6:i*6+6])
    return l

def check(s):
    l=[]
    for i in s:
        if beetwen(i,l)==False:
            print('key has wrong coordinates')
            return 0
        l.append(i)
    if len(s)!=9:
        print('key should be 9 coordinates long')
        return 0
    return 1

def main(st,k=generator()):
    l=[]
    if check(k)==0 :
        return 'cancelling the program'
    if len(st)>108:
        print(len(st))
        return 'Line should be less than 108 chars'
    if len(st)<=36:
        for i in range(36-len(st)): st+='.'
        m=1
    if len(st)>36 and len(st)<=72:
        if len(st)<=72:
            for i in range(72-len(st)): st+='.'
        m=2
    if len(st)>72 and len(st)<=108:
        if len(st)<=108:
            for i in range(108-len(st)): st+='.'
        m=3
    for i in range(m): l.append(cut(st[i*36:i*36+36]))
    s=''
    for j in range(len(l)):
        for i in k: s+=l[j][int(i[0])][int(i[1])]
        for i in k: s+=l[j][int(i[0])][int(reject(i[1]))]
        for i in k: s+=l[j][int(reject(i[0]))][int(i[1])]
        for i in k: s+=l[j][int(reject(i[0]))][int(reject(i[1]))]
    print(s)
    print()
    print('Ключ для расшифровки: ',k)
    
def dmain(st,k):
    s=''
    if check(k)==False : return 'cancelling the program'
    l=[]
    a=[]
    for i in range(len(st)//36): a.append(st[i*36:i*36+36])
    st=a        
    for j in range(len(st)):
        for i in range(len(st[j])//len(k)):
            l.append(st[j][i*len(k):i*len(k)+len(k)])
    for i in range(6):
        for j in range(6):
            for n in range(len(l)):
                for z in range(len(k)):
                    if n == 0 or n == 4 or n == 8:
                        if int(k[z][0])==i and int(k[z][1])==j:
                            s+=l[n][z]
                    if n == 1 or n == 5 or n == 9:
                        if int(k[z][0])==i and int(reject(k[z][1]))==j:
                            s+=l[n][z]
                    if n == 2 or n == 6 or n == 10:
                        if int(reject(k[z][0]))==i and int(k[z][1])==j:
                            s+=l[n][z]
                    if n == 3 or n == 7 or n == 11:
                        if int(reject(k[z][0]))==i and int(reject(k[z][1]))==j:
                            s+=l[n][z]

    if len(st)==2: s=s[::2]+s[1::2]
    if len(st)==3: s=s[::3]+s[1::3]+s[2::3]
    print(s)           
                  



