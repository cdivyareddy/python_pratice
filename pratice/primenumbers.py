min=int(input())
max=int(input())
for i in range(min,max+1):
               count=0
               for j in range(1,i+1):
                            count+=1
                            if(count==2):
                                    print(i,end=' ')
