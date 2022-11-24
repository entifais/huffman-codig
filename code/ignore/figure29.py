def getprob(text):
    """
    getprob(l)->tabla
    get proabiliti of ocurrences in list, can be usen in list and strings
    """
    tabla = dict()
    for i in text:
        if  i in tabla:
            tabla[i]= tabla[i]+1
        else:
            tabla[i] = 1
    return tabla
 
def build_heap(A, n):
    elemento = 1
    while elemento < n:
        heapify(A, elemento)
        elemento = elemento + 1
 
def heapify(A, n):
    base = n
    while base > 0 and A[A[base]] < A[A[(base-1)//2]]:
        tmp = A[base]
        A[base] = A[(base-1)//2]
        A[(base-1)//2] = tmp
        base = (base-1)//2    
    
def sift(A, n):
    base = 0
    minimo = base
    while base < n: 
        if 2*base + 1 < n and A[A[2*base+1]] < A[A[minimo]]:
            minimo = 2*base+1
        if 2*base+2 < n and  A[A[2*base+2]] < A[A[minimo]]:
            minimo = 2*base+2
        if base != minimo:
            tmp =A[base]
            A[base] = A[minimo]
            A[minimo] = tmp
            base = minimo
        else:
            base = n        
 
def codeLengh(tabla):
    n = len(tabla)
    A = [0] * (2*n)
    i = 0
    while i < n:
        A[i] = n + i
        A[n+i] = tabla[i]
        i = i + 1
    build_heap(A, n)
    h = n-1
    while h > 0:
        m1 = A[0]
        A[0] = A[h]
        h = h - 1
        sift(A,h)
        m2 = A[0]
        A[h+1] = A[m1]+A[m2]
        A[0] = h+1
        A[m1] = h + 1
        A[m2] = h+1
        sift(A, h)
    A[1] = 0
    i = 2
    while i < 2*n:
        A[i] = A[A[i]]+1
        i = i + 1
    return A
    
tablaOriginal = getprob("aaaaabbbbbccccccccccddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffgggggggggg")
simbolos = list(tablaOriginal.keys())
tabla = list(tablaOriginal.values())
A = codeLengh(tabla)
i = 0
simbolsdict=dict()
while i < len(simbolos):
    simbolsdict[simbolos[i]]= A[len(simbolos)+i]
    print(simbolos[i], ": ", A[len(simbolos)+i])
    i = i + 1
        
    
    
    
def figure29(table,maxlength,fristcode):
    numl=[0]*len(table)#for 1 llena el arreglo de 0
    #n es la cantidad de simbolos
    #li es la frecuencia
    n=len(tabla)
    for i in range(n):
        numl[tabla[i]]=numl[tabla[i]]+1
    fristCode=[0]*maxlength#fristCode[maxlength]# 
    for l in range(1,maxlength-1,-1):
        fristCode[l]=(fristCode[l+1]+numl[l+1])/2
    nextcode=[]
    for l in range(maxlength):
        nextcode.append(fristCode[l])
    codeword=[]
    symbol=[0]*(len(nextcode)-len(fristcode))
    for i in range(symbol):
    symbol[i]=[0]*n
    for i in range(n):
    #parte que ni puta idea
        codeword.append(nextcode[tabla[i]])
        symbol[tabla[i]][nextcode[tabla[i]-fristcode[l]]
        nextcode[tabla[i]]=nextcode[tabla[i]+1]
 
figure29(simbolsdict,max(A),symbol)