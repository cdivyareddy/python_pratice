# lambda
whis=lambda :'hlo'
print(whis())

#max
l=[34,45,23,59,78]
print(max(l,key=lambda num:num%10))
#sorted
l=[908,345,567,890,345]
print(sorted(l,key=lambda num:num%10))
#1
s='we are in class'
st=s.split()
l=sorted(st,key=lambda word:len(word))
print(' '.join(l))
#2
s='we are in class'
l=max(s.split(),key=lambda word:len(word))
print(l)
#
lst=[2,2,2,2,2,3,3,3,4,4,4,5,5]
print(sorted(lst,key=lambda num:lst.count(num)))

lst=['we','are','in','class']
m=list(map(len,lst))
print(m)

m=list(map(lambda count:count*'*',range(5,0,-1)))
print('\n'.join(m))

m=list(map(lambda count:count*'*',range(1,6)))
print('\n'.join(m))

m=list(map(lambda count,num:count*str(num),range(1,6),range(1,6)))
print('\n'.join(m))

from functools import reduce
s=reduce(lambda fsum,num:fsum+num,range(1,6))
print(s)

s=reduce(lambda mul,num:mul*num,range(1,6),1)
print(s)


#comperhensions

lt=[2,3,4,5]
n_lt=[num*10 for num in lt]
print(n_lt)

lt=[2,3,4,5]
n_lt=[num for num in lt if num%2==0]
print(n_lt)

lt=[2,3,4,5]
n_lt=[num for num in lt if num%2!=0]
print(n_lt)


lt=[2,3,0,4,0,5,0,3,9]
n_lt=[num for num in lt if num!=0]+[num for num in lt if num==0]
print(n_lt)

st1='abc'
st2='mno'
n_lt=[ch+ch1 for ch in st1 for ch1 in st2]
print(n_lt)

l=[7,8,9,0]
n=(n*10 for n in l)
print(list(n))

st='engineering'
d={ch:st.count(ch) for ch in st}
print(d)

d={10:'a',20:'b',30:'c'}
di={ v:k for k,v in d.items()}
print(di)

d=dict(zip(d.values(),d.keys()))
print(d)

st='amit smoke only kings'
st1=st.split()
n_st=[ word[::-1] for word in st1]
print(' '.join(n_st))

'''

s='i2s th1is ques4tion exa3m'
st=s.split()
n_ls=[word for word in st for ch in word if '0'<=ch<='9'

'''
s='i2s th1is ques4tion exa3m'
lst=st.split()
d={}
for word in lst:
    new_word=''
    dig=''
    for ch in word:
        if'0'<=ch<='9':
            dig+=ch
        else:
            new_word+=ch
        d[int(dig)]=new_word
m=map(lambda key:d[key],range(1,len(lst)+1))
print(' '.join(m))












