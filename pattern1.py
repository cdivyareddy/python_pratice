for star in range(1,6):
    print('*'*star)
for star in range(5,0,-1):
    print('*'*star)
for space,star in  zip(range(4,-1,-1),range(1,6)):
                       print('-'*space,'*'*star,sep='')
for space,star in  zip(range(4,0,-1),range(1,11,2)):
                       print('-'*space,'*'*star,sep='')                         
for num,count in  zip(range(1,6),range(5,0,-1)):
                       print(str(num)*count)                         
for space,num,count in  zip(range(4,-1,-1),range(5,0,-1),range(1,6)):
                       print(str(num)*count)                         
for space,num,count in  zip(range(4,-1,-1),range(5,0,-1),range(1,6)):
                       print(space*'-',str(num)*count,sep='')                         
for space,star in  zip(range(0,4),range(4,0,-1)):
                       print('-'*space,'*'*star,sep='')                   
for space,num,count in  zip(range(4,-1,-1),range(5,0,-1),range(1,6)):
                       print(space*'-',str(num)*count,sep='')  
for num,count in zip(range(1,5),range(4,0,-1)):
    print(str(num)*count)
for space,num,count in  zip(range(0,4),range(1,5),range(4,0,-1)):
                       print(space*'-',str(num)*count,sep='') 

for num,count in  zip(range(4,0,-1),range(1,5)):
                       print(str(num)*count)
for space,num,count in  zip(range(3,-1,-1),range(4,0,-1),range(1,5)):
                       print(space*'-',str(num)*count,sep='')  
for num,count in  zip(range(5,0,-1),range(5,0,-1)):
                       print(str(num)*count)
for num,count in  zip(range(1,6),range(1,6)):
                       print(str(num)*count)
for space,num,count in  zip(range(0,5),range(5,0,-1),range(5,0,-1)):
                       print(space*'-',str(num)*count,sep='')
for space,num,count in  zip(range(4,-1,-1),range(1,6),range(1,6)):
                       print(space*'-',str(num)*count,sep='')
