l=[3,4,5]
copy=l
print(l is copy)
l[0]=6
print(l,copy)

l=[3,4,5]
copy=l[::]
print(l is copy)
l[0]=6
print(l,copy)

import copy
l=[3,4,5]
copy=l.copy()
print(l is copy)
l[0]=6
print(l,copy)

import copy
l=[3,4,5]
copy=copy.copy(l)
print(l is copy)
l[0]=6
print(l,copy)



import copy
l=[[3,4,5],[9,7,0]]
copy=copy.deepcopy(l)
print(l is copy)
l[0][1]=6
print(l,copy)

import copy
l={3:6,4:7,5:8}
copy=copy.deepcopy(l)
print(l is copy)
l[3]=8
print(l,copy)
