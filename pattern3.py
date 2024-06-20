#1.1
for ev in range(5,0,-1):
    for num in range(1,ev):
        print(num,end='')
    print()
#1.2
for ev in range(5,0,-1):
    num=1
    while(num!=ev):
        print(num,end='')
        num+=1
    print()
#1.3    
for ev in range(5,0,-1):
    print(*list(range(1,ev)),sep='')
#2.1
for ev in range(2,6):
    for num in range(1,ev):
        print(num,end='')
    print()
#2.2
for ev in range(2,6):
    num=1
    while(num!=ev):
        print(num,end='')
        num+=1
    print()
#2.3   
for ev in range(2,6):
    print(*list(range(1,ev)),sep='')
#3.1
for space,sv in zip(range(0,4),range(4,0,-1)):
    print(space*'-',end='')
    for num in range(sv,0,-1):
        print(num,end='')
    print()
#3.2
for space,sv in zip(range(0,4),range(4,0,-1)):
    print(space*'-',end='')
    num=sv
    while(num!=0):
        print(num,end='')
        num-=1
    print()
#3.3
for space,sv in zip(range(0,4),range(4,0,-1)):
    print(space*'-',*list(range(sv,0,-1)),sep='')
#4.1
for space,sv in zip(range(3,-1,-1),range(1,5)):
    print(space*'-',end='')
    for num in range(sv,0,-1):
        print(num,end='')
    print()
#4.2
for space,sv in zip(range(3,-1,-1),range(1,5)):
    print(space*'-',end='')
    num=sv
    while(num!=0):
        print(num,end='')
        num-=1
    print()
#4.3
for space,sv in zip(range(3,-1,-1),range(1,5)):
    print(space*'-',*list(range(sv,0,-1)),sep='')
    
#5.1
for sv in range(1,5):
    for num in range(sv,5):
        print(num,end='')
    print()
#5.2
for sv in range(1,5):
    num=sv
    while(num!=5):
        print(num,end='')
        num+=1
    print()
#5.3
for sv in range(1,5):
    print(*list(range(sv,5)),sep='')
#6.1
for space,ev in zip(range(0,4),range(0,4)):
    print(space*'-',end='')
    for num in range(4,ev,-1):
        print(num,end='')
    print()
#6.2
for space,ev in zip(range(0,4),range(0,4)):
    print(space*'-',end='')
    num=4
    while(num!=ev):
        print(num,end='')
        num-=1
    print()
#6.3
for space,ev in zip(range(0,4),range(0,4)):
    print(space*'-',*list(range(4,ev,-1)),sep='')
#7.1
for space,sv in zip(range(3,-1,-1),range(4,0,-1)):
    print(space*'-',end='')
    for num in range(sv,5):
        print(num,end='')
    print()
#7.2
for space,ev in zip(range(3,-1,-1),range(4,0,-1)):
    print(space*'-',end='')
    num=ev
    while(num!=5):
        print(num,end='')
        num+=1
    print()
#7.3
for space,sv in zip(range(3,-1,-1),range(4,0,-1)):
    print(space*'-',*list(range(sv,5)),sep='')
#8.1
for sv in range(4,0,-1):
    for num in range(sv,5):
        print(num,end='')
        
    print()
#8.2
for sv in range(4,0,-1):
    num=sv
    while(num!=5):
        print(num,end='')
        num+=1
    print()
#8.3
for sv in range(4,0,-1):
    print(*list(range(sv,5)),sep='')
#9.1
for sv in range(4,0,-1):
    for num in range(sv,0,-1):
        print(num,end='')
    print()
#9.2
for sv in range(4,0,-1):
    num=sv
    while(num!=0):
        print(num,end='')
        num-=1
    print()
#9.3
for sv in range(4,0,-1):
    print(*list(range(sv,0,-1)),sep='')   
#10.1
for ev in range(3,-1,-1):
    for num in range(4,ev,-1):
        print(num,end='')
    print()
#10.2
for ev in range(3,-1,-1):
    num=4
    while(num!=ev):
        print(num,end='')
        num-=1
    print()
#10.3
for ev in range(3,-1,-1):
    print(*list(range(4,ev,-1)),sep='') 
#11.1
for space,sv in zip(range(0,4),range(1,5)):
    print(space*'-',end='')
    for num in range(sv,5):
        print(num,end='')
    print()
#11.2
for space,sv in zip(range(0,4),range(1,5)):
    print(space*'-',end='')
    num=sv
    while(num!=5):
        print(num,end='')
        num+=1
    print()
#11.3
for space,sv in zip(range(0,4),range(1,5)):
    print(space*'-',*list(range(sv,5)),sep='')
#12.1
for space,sv in zip(range(3,-1,-1),range(4,0,-1)):
    print(space*'-',end='')
    for num in range(sv,5):
        print(num,end='')
    print()
#12.2
for space,sv in zip(range(3,-1,-1),range(4,0,-1)):
    print(space*'-',end='')
    num=sv
    while(num!=5):
        print(num,end='')
        num+=1
    print()
#12.3
for space,sv in zip(range(3,-1,-1),range(4,0,-1)):
    print(space*'-',*list(range(sv,5)),sep='')
#13.1
for sv in range(4,0,-1):
    for num in range(sv,0,-1):
        print(num,end='')
    print()
#13.2
for sv in range(4,0,-1):
    num=4
    while(num!=sv):
        print(num,end='')
        num-=1
    print()
#13.3
for ev in range(4,0,-1):
    print(*list(range(sv,0,-1)),sep='')
#14.1
for sv in range(1,5):
    for num in range(sv,0,-1):
        print(num,end='')
    print()
#14.2
for sv in range(1,5):
    num=sv
    while(num!=0):
        print(num,end='')
        num-=1
    print()
#14.3
for sv in range(1,5):
    print(*list(range(sv,0,-1)),sep='') 

#15.1
for sv in range(1,5):
    for num in range(sv,0,-1):
        print(num,end='')
    print()
#15.2
for sv in range(1,5):
    num=sv
    while(num!=0):
        print(num,end='')
        num-=1
    print()
#15.3
for sv in range(1,5):
    print(*list(range(sv,0,-1)),sep='') 
#16.1
for space,sv in zip(range(0,4),range(5,1,-1)):
    print(space*'-',end='')
    for num in range(1,sv):
        print(num,end='')
    print()
#16.2
for space,sv in zip(range(0,4),range(5,1,-1)):
    print(space*'-',end='')
    num=1
    while(num!=sv):
        print(num,end='')
        num+=1
    print()
#16.3
for space,sv in zip(range(0,4),range(5,1,-1)):
    print(space*'-',*list(range(1,sv)),sep='')

#16.1.1
for space,ev in zip(range(3,-1,-1),range(2,6)):
    print(space*'-',end='')
    for num in range(1,ev):
        print(num,end='')
    print()
#16.1.2
for space,ev in zip(range(3,-1,-1),range(2,6)):
    print(space*'-',end='')
    num=1
    while(num!=ev):
        print(num,end='')
        num+=1
    print()
#16.1.3
for space,ev in zip(range(3,-1,-1),range(2,6)):
    print(space*'-',*list(range(1,ev)),sep='')
