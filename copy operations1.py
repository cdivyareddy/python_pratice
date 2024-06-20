l=[4,5,6]
a=l
print(a is l)
l[0]=2
print(l,a)

l=[4,5,6]
a=l[::]
print(a is l)
l[0]=2
print(l,a)

import copy
l=[4,5,6]
a=l.copy()
print(a is l)
l[0]=2
print(l,a)

import copy
l=[4,5,6]
a=copy.copy(l)
print(a is l)
l[0]=2
print(l,a)

import copy
l=[4,5,6]
a=copy.deepcopy(l)
print(a is l)
l[0]=2
print(l,a)
 
