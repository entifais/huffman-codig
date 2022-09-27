from tools import *

txt=input("input a strint to encode:\n")
prob=getprob(txt)
print(prob,len(prob))
data=[]
for i in prob:
	data.append(pair(prob[i],i))
h=heapMin(len(prob))
for i in data:
	h.insert(i)

vals=[]
h.p3()
while len(h)>3:
	tmp1=h.pop()
	tmp2=h.pop()
	conc=str(tmp1.second)+str(tmp2.second)
	h.insert(pair(tmp1.first+tmp2.first,conc))


#encode data 10101..
#decode data abc..
print()