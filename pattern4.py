#1
for star in range(1,6):
    print('*'*star)
#2    
for star in range(5,0,-1):
    print('*'*star)
#3
space,star=4,1
while(star!=6):
    print('-'*space,'*'*star,sep='')
    space-=1
    star+=1
#3.1
for space,star in zip(range(4,-1,-1),range(1,6)):
                      print('-'*space,'*'*star,sep='')
#4
num,count=1,4
while(num!=5):
    print(str(num)*count)
    num+=1
    count-=1
#4.1
for num,count in zip(range(1,5),range(4,0,-1)):
    print(str(num)*count)
#5
num,count=1,1
while(num!=6):
    print(str(num)*count)
    num+=1
    count+=1    
#5.1
for num,count in zip(range(1,6),range(1,6)):
    print(str(num)*count)
#6
space,num,count=4,5,1
while(num!=0):
    print(space*'-',str(num)*count,sep='')
    space-=1
    num-=1
    count+=1
#6.1
for space,num,count in zip(range(4,-1,-1),range(5,0,-1),range(1,6)):
    print(space*'-',str(num)*count,sep='')
       
