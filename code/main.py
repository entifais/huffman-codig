from tools import *

txt=input("input a strint to encode:\n")
prob=getprob(txt)
print(prob,len(prob))
data=[]
for i in prob:
	data.append(pair(prob[i],i))
h=heapMin(len(prob))
for i in data:
	#print(i)
	h.insert(i)

vals=[]
#for i in h.getheap():
h.p3()
while len(h)>3:
	tmp1=h.pop()
	tmp2=h.pop()
	#print(tmp1,tmp2)
	conc=str(tmp1.second)+str(tmp2.second)
	#print(conc)
	h.insert(pair(tmp1.first+tmp2.first,conc))

#print(len(h))

	#node(,l=tmp1,r=tmp2)
	#vals.append()
#print(,type(h.getheap()[1]))


#encode data 10101..
#decode data abc..
print()