'''for star in range(1,6):
    print(star*'*')

num=1
while num!=6:
    print(num*'*')
    num+=1

    
for star in range(5,0,-1):
    print(star*'*')

for space,star in zip(range(1,4),range(5,0,-1)):
    print(space*"-",star*'*',sep='')

    
star=5
space=0
while star!=0:
    print(space*"-",star*'*',sep='')
    star-=1
    space+=1


for num,space,count in zip(range(5,0,-1),range(4,-1,-1),range(1,6)):
    print('-'*space,str(num)*count,sep='')
    
ch=97
for i in range(1,6):
    print(chr(ch)*i)
    ch+=1


for ev in range(4,-1,-1):
    for num in range(5,ev,-1):
        print(num,end='')
    print()

for sv in range(1,6):
    for num in range(sv,0,-1):
        print(num,end='')
    print()
for sv in range(1,6):
    num=sv
    while num!=0:
        print(num,end='')
        num-=1
    print()

for space,sv in zip(range(4,-1,-1),range(5,0,-1)):
    print(space*'-',end='')
    for num in range(sv,6):
        print(num,end='')
    print()

for ev in range(5,0,-1):
    for num in range(1,ev):
        print(num,end='')
    print()

for space,sv in zip(range(3,-1,-1),range(1,5)):
    print(space*'-',end='')
    for num in range(sv,0,-1):
        print(num,end='')
    print()'''



for i in range(7):
    for j in range(7):
        if(i==0 and 1<=j<=6) or (i==3 and 1<=j<=5) or (i==6 and 0<=j<=5) or (j==0 and 1<=i<=2) or (j==6 and 4<=i<=5):
            print('*',end='')
        else:
            print('',end='')


    
                                         
