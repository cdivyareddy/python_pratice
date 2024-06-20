for star in range(1,5):
    print(star*'*')
    
for star in range(5,0,-1):
    print(star*'*')
    
for space,star in zip(range(4,-1,-1),range(1,6)):
    print(space*' -',star*' *',sep='')
    
for num,count in zip(range(1,5),range(4,0,-1)):
    print(str(num)*count)
    
for num,count in zip(range(1,6),range(1,6)):
    print(str(num)*count)

for space,num,count in zip(range(4,-1,-1),range(1,6),range(1,6)):
    print(space*'-',str(num)*count,sep='')


for lines in range(1,5):
    for col in range(lines):
        print('*',end='')
    print()
    
for lines in range(1,5):
    col=0
    while(col!=lines):
        print('*',end='')
        col+=1
    print()
for ev in range(4,-1,-1):
    for num in range(5,ev,-1):
        print(num,end='')
    print()
