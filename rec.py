import random
import itertools

def crypt(st):
    print('Choose crypt style: 0 - fullauto, 1 - all by your hands(there is also a secret)')
    s=str(input())
    l=2*2
    g=1 
    print('Message length: ',len(st))
    if s==str(0):
        x=2
        y=2
        while l<len(st):
            if y!=x: y+=2
            else: x+=2
            l=x*y
        if len(st)<l:
            st+='.'*(l-len(st))
        print('Resulution message length: ',len(st))
        k=generator(x,y)
        if check(k,x,y)==False: return 'something went wrong'
        
        
    if s==str(1):
        print('length: ')
        x=int(input())
        print('width:')
        y=int(input())
        l=x*y
        if x%2!=0 or y%2!=0 or x==0 or y==0: return 'x and y should be equal(2,4,6...)'
        if l<len(st):
            if len(st)/l-len(st)//l==0: g=len(st)//l
            else: g=len(st)//l+1
        if len(st)<l:
            st+='.'*(l-len(st))
        print('key: ')
        k=[]
        for i in range((x*y)//4):
            z=input()
            k.append((int(z[0]),int(z[1])))
        if len(k)!=(x*y)//4: return 'key should have ',(x*y)//4, ' arguments'
        if check(k,x,y)!=True: return 'invalid key'
        
    if s!=str(0) and s!=str(1): return 'choose alredy something (0 or 1)'
    print('Key: ',k)
    print()
    print('X and Y: ',x,y)
    print()
    z=[]
    n=[]
    while len(st)<l*g:
        st+='.'
    for i in range(g): 
        z.append(st[i*l:i*l+l])
    for i in range(len(z)):
        r=[]
        for j in range(x):
            r.append(z[i][j*y:y*j+y])
        n.append(r)
    s=''
    for i in n:
        for t in k:
            s+=i[t[0]][t[1]]
            s+=i[t[0]][reject(t[1],y)]
            s+=i[reject(t[0],x)][t[1]]
            s+=i[reject(t[0],x)][reject(t[1],y)]
    print(s)        

def check(k,x,y):
    l=[]
    g=[]
    T=True
    for i in k:
        g.append((i[0],i[1]))
        g.append((reject(i[0],x),i[1]))
        g.append((reject(i[0],x),reject(i[1],y)))
        g.append((i[0],reject(i[1],y)))
        for j in g:
            if j in l: T=False
        g=[]
        l.append(i)
    return T

def reject(s,a):
    return a-1-s


def generator(x,y):
    a=(x*y)//4
    x1=[]
    y1=[]
    for i in range(x):
        x1.append(i)
    for i in range(y):
        y1.append(i)    
    l=[]
    while len(l)<a:
        T=True
        g=[]
        x2=random.choice(x1)
        y2=random.choice(y1)
        g.append((x2,y2))
        g.append((reject(x2,x),y2))
        g.append((reject(x2,x),reject(y2,y)))
        g.append((x2,reject(y2,y)))
        for i in g:
            if i in l: T=False
        if T==True: l.append((x2,y2))
    return l 






def decrypt(st,k):
    print('Choose decrypt style: 0 - fullauto, 1 - all by your hands')
    s=int(input())
    l=2*2
    g=1 
    print('Message length: ',len(st))
    if s==0:
        x=2
        y=2
        while l<len(st):
            if y!=x: y+=2
            else: x+=2
            l=x*y
        if check(k,x,y)==False: return 'something went wrong'
        
    if s==1:
        print('length: ')
        x=int(input())
        print('width:')
        y=int(input())
        l=x*y
        if x%2!=0 or y%2!=0 or x==0 or y==0: return 'x and y should be equal(2,4,6...)'
        if l<len(st):
            if len(st)/l-len(st)//l==0: g=len(st)//l
            else: g=len(st)//l+1
        if len(k)!=(x*y)//4: return 'key should have ',(x*y)//4, ' arguments'
        if check(k,x,y)!=True: return 'invalid key'

    if s!=0 and s!=1: return 'choose alredy something (0 or 1)'
    print('Key: ',k)
    print()
    print('X and Y: ',x,y)
    print()
    z=[]
    n=[]
    while len(st)<l*g:
        st+='.'
    for i in range(g): 
        z.append(st[i*l:i*l+l])
    for i in range(len(z)):
        r=[]
        for j in range(x):
            r.append(z[i][j*y:y*j+y])
        n.append(r)
    s=''
    z=n
    a=[]
    for i in range(len(z)):
        b=[]
        for j in range(len(z[i])):
            c=[]
            for v in range(len(z[i][j])):
                c.append(z[i][j][v])
            b.append(c)
        a.append(b)
    f=[]
    m=[]
    w=(len(st)//len(a))//4
    for j in range(len(st)//4):
        m.append(st[j*4:j*4+4])
    for i in range(g):
        f.append(m[i*w:i*w+w])
    for i in range(len(z)):
        for t in range(len(k)):
            a[i][k[t][0]][k[t][1]]=f[i][t][0]
            a[i][k[t][0]][reject(k[t][1],y)]=f[i][t][1]
            a[i][reject(k[t][0],x)][k[t][1]]=f[i][t][2]
            a[i][reject(k[t][0],x)][reject(k[t][1],y)]=f[i][t][3]
    for i in a:
        for j in i:
            for n in j:
                s+=n
    print(s)
        



        
