#1
num=12345678
dsum=0
while(num!=0):
    ld=num%10
    num//=10
    fcount=0
    for fa in range(1,ld+1):
        if(ld%fa==0):
            fcount+=1
    if(fcount==2):
        dsum+=ld
print(dsum)

#2
for num in range(23,44):
    fcount=0
    for fa in range(1,num+1):
        if(num%fa==0):
            fcount+=1
    if(fcount==2):
        print(num)
#3       
for num in range(43,22,-1):
    fcount=0
    for fa in range(1,num+1):
        if(num%fa==0):
            fcount+=1
    if(fcount==2):
        print(num)
#4
max=0
for num in range(10,50):
    fcount=0
    for fa in range(1,num+1):
        if(num%fa==0):
            fcount+=1
    if(fcount==2):
        if(max<num):
            max=num
print(max)
#5
for num in range(100,999):
    fcount=0
    for fa in range(1,num+1):
        if(num%fa==0):
            fcount+=1
    if(fcount==2):
        print(num,end=' ,')
#6       
l=[]
for num in range(1,30):
    fcount=0
    for fa in range(1,num+1):
        if(num%fa==0):
            fcount+=1
    if(fcount==2):
        list=l.append(num)
for i in range(len(l)):
    if(i%2==0):
        print(l[i])

        
        

