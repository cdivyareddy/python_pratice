#prime
def is_prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount
def prime(num):
    return is_prime(num)==2

#composite
def is_prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount
def composite(num):
    return is_prime(num)>2




#perfect
def is_perfect(num,dsum=0):
    for fa in range(1,num):
        if num%fa==0:
            dsum+=fa
    return num==dsum
            


#perfect

def fact(num,dsum=0):
    for fa in range(1,num):
        if num%fa==0:
            dsum+=fa
    return dsum
def is_perfect(num):
    return num==fact(num)

#pronic

def number(num):
    n=0
    while(n*(n+1)<num):
        n+=1
    return n*(n+1)   
def is_pronic(num):
    return num== number(num)


#sunny

def number(num):
    n=0
    while(n*n <(num+1)):
        n+=1
    return n*n
def is_sunny(num):
    return (num+1)==number(num)


#palindrome
def reverse(num,rev=0):
    while(num!=0):
        ld=num%10
        rev=rev*10+ld
        num//=10
    return rev

def is_palindrome(num):
    return num==reverse(num)

#niven
def dig_sum(num,dsum=0):
    while num!=0:
        ld=num%10
        dsum+=ld
        num//=10
    return dsum
def niven(num):
    return (num)%dig_sum(num)==0

        
#spy
def dig_sum(num,dsum=0):
    while num!=0:
        ld=num%10
        dsum+=ld
        num//=10
    return dsum
def is_prod(num,prod=1):
    while num!=0:
        ld=num%10
        prod*=ld
        num//=10
    return prod
def is_spy(num):
    return is_prod(num)==dig_sum(num)


#paly prime
def prime(num,fcount=0):
    for fa in range(1,num+1):
        if(num%fa==0):
            fcount+=1
    return fcount==2

def reverse(num,rev=0):
    while(num!=0):
        ld=num%10
        rev=rev*10+ld
        num//=10
    return rev

def is_palindrome(num):
    return prime(num) and num==reverse(num)


#emirp

def prime(num,fcount=0):
    for fa in range(1,num+1):
        if(num%fa==0):
            fcount+=1
    return fcount==2

def reverse(num,rev=0):
    while(num!=0):
        ld=num%10
        rev=rev*10+ld
        num//=10
    return rev

def rev_prime(rev,fcount=0):
    for fa in range(1,rev+1):
        if rev%fa==0:
            fcount+=1
    return fcount==2
        
    

def is_emirp(num):
    return prime(num) and num!=reverse(num) and rev_prime(num)

#amstrong
def sum_digit(num,dsum=0):
    count=len(str(num))
    while num!=0:
        ld=num%10
        dsum+=ld**count
        num//=10
    return dsum
        
def is_arms(num):
    return num==sum_digit(num)


#disarim
def sum_digit(num,dsum=0):
    while num!=0:
        ld=num%10
        dsum+=ld**len(str(num))
        num//=10
    return dsum
        
def is_disarim(num):
    return num==sum_digit(num)

#strong
def fact(num,dsum=0):
    while num!=0:
        ld=num%10
        fac=1
        for fa in range(ld,0,-1):
            fac*=fa
        dsum+=fac
        num//=10
    return dsum
def is_strong(num):
    return num==fact(num)

#happy number
def one(num):
    while num>9:
        dsum=0
        while(num!=0):
            ld=num%10
            dsum+=ld**2
            num//=10
        num=dsum
    return num
def is_happy(num):
    return one(num)==1



#automarphic
def rem(num):
    square=num**2
    count=len(str(num))
    reminder=square%(10**count)
    return reminder

def is_auto(num):
    return num==rem(num)

#trymarphic
def rem(num):
    square=num**3
    count=len(str(num))
    reminder=square%(10**count)
    return reminder

def is_auto(num):
    return num==rem(num)

#neno
def sum(num,dsum=0):
    square=num**2
    while square!=0:
        
        ld=square%10
        dsum+=ld
        square//=10
    return dsum
def is_neno(num):
    return num==sum(num)

#evil
def binary(num,count=0):
    while num!=0:
        rem=num%2
        count+=rem
        num//=2
    return count%2==0
    
def is_evil(num):
    return binary(num)
print(is_evil(15))
#tech
def half(num):
    sum,n1,n2=0,0,0
    count=len(str(num))//2
    ld=num%(10**count)
    n1+=ld
    n2+=num//(10**count)
    sum=n1+n2
    p=sum**2
    return p
def is_tech(num):
    return num==half(num)


#fascinating
def number(num):
    c=str(num*1)+str(num*2)+str(num*3)
    for n in c:
        flag=0
        if len(c)!=9 or c.count(n)>1 or c.count(n)==0:
            flag=1
    return flag!=1
def is_fas(num):
    return number(num)

            
            

