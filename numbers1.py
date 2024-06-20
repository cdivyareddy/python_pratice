'''num=145
copy=num
dsum=0
while(num!=0):
    ld=num%10
    fact=1
    for n in range(ld,0,-1):
        fact*=n
    dsum+=fact
    num//=10
print('strong'if copy==dsum else 'not strong')
    
        
num=49
copy=num
dsum=0
while num>9:
    dsum=0
    while(num!=0):
        ld=num%10
        dsum+=ld**2
        num//=10
    num=dsum
print('happy' if(num==1) else 'not happy')

num=125
square=num**2
count=len(str(num))
rem=square%(10**count)
print('automarphic' if(rem==num) else 'not automarphic')

num=27
square=num**3
count=len(str(num))
rem=square%(10**count)
print('trymarphic' if(rem==num) else 'not tryomarphic')

num=78
copy=num
sum=0
square=num**2
while(square!=0):
    ld=square%10
    sum+=ld
    square//=10
print('neno' if(copy==sum) else 'not neno')

num=14
count=0
while(num!=0):
    rem=num%2
    count+=rem
    num//=2
print('evil' if(count%2==0) else 'not evil')
num=2025
sum=0
n1,n2=0,0
count=len(str(num))//2
ld=num%(10**count)
n1+=ld
n2+=num//10**count
sum=n1+n2
p=sum**2
print('tech' if(p==num) else 'not tech')'''
num=192
n1=num*2
n2=num*3
con=str(num)+str(n1)+str(n2)
c=int(con)
while(c!=0):
    ld=c%10
    c//=10
for n in range(1,10):
    pass
else:
    if(n==ld):
        print('fas')
    else:
        print('not fas')
            
            

    



