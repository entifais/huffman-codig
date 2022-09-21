from tools import *

txt=input("input a strint to encode:\n")
prob=getprob(txt)
print(prob,len(prob))
h=heapMin(len(prob))
for i in prob:
	h.insert(float(prob[i]))
h.p()
#encode data 10101..
#decode data abc..
print()