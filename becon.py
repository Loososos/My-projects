alf = 'абвгдеёжзийклмнопрстуфхцчшщьыэюя'
alf1=alf[:16]
alf2=alf[16:]
import random
import itertools

# формирование библиотеки букв в двоичной системе
cod=[]
for i in itertools.product('01',repeat=5):
    s=''
    for j in range(5):
        s+=i[j]
    cod.append(s)

def normalize(st):
    '''Функция удаляет ненужные символы во входящей строке'''
    newst = ''
    st = st.lower()
    for i in st:
        if i in alf:
            newst += i
    return newst

# формирование массивов с четными и нечетными буквами
alf21=''
alf22=''
for i in range(len(alf)):
        if i%2==0: alf21+=alf[i]
        if i%2!=0: alf22+=alf[i]


def try1(st,m=1):
    st=normalize(st)
    s=''
    l=''
    for i in st: s+=cod[alf.index(i)]
    for i in s:
        if i==str(0): l+='а'
        if i==str(1): l+='a'
    if m==0: print(s)
    if m==1: print(l)
        
def dtry1(st):
    s=[]
    for i in range(len(st)//5): s.append(st[i*5:i*5+5])
    st=[]
    z=[]
    for i in range(len(s)):
        for j in s[i]:
            if (j==str(0) or j in alf): z+=str(0)
            if (j==str(1) or j not in alf) and j!=str(0): z+=str(1)
    st=''
    s=[]
    for i in z: st+=i
    for i in range(len(st)//5): s.append(st[i*5:i*5+5])
    st=''
    for i in s:
        st+=alf[cod.index(i)]
    print(st)



    
def try2(st,m=0):
    s=''
    st=normalize(st)
    for i in st: s+=cod[alf.index(i)]
    st=''
    if m==0:
        for i in s:
            if i==str(0): st+=random.choice(alf1)
            if i==str(1): st+=random.choice(alf2)
    if m==1:
        for i in s:
            if i==str(0): st+=random.choice(alf21)
            if i==str(1): st+=random.choice(alf22)
    if m!=0 and m!=1: return 'You need to choose m(0 or 1)'
    print(st)
    




def dtry2(st,m):
    s=''
    if m==0:
        for i in st:
            if i in alf1: s+=str(0)
            if i in alf2: s+=str(1)
    if m==1:
        for i in st:
            if i in alf21: s+=str(0)
            if i in alf22: s+=str(1)
    if m!=0 and m!=1: return 'You need to choose m(0 or 1)'
    st=[]
    for i in range(len(s)//5): st.append(s[i*5:i*5+5])
    s=''
    for i in st: s+=alf[cod.index(i)]
    print(s)
