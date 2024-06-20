
'''
n=324
c=n
s=0
while n!=0:
    ld=n%10
    s+=ld
    n//=10
print( 'niven' if c%s==0 else 'not n')


def pal(n,s=0):
    while n!=0:
        ld=n%10
        s=s*10+ld
        n//=10
    return s
def is_pal(n):
    return n==pal(n)
print(is_pal(102))

def pal(n,s=0):
    while n!=0:
        ld=n%10
        s=s*10+ld
        n//=10
    return s
def prime(n,fc=0):
    for fa in range(1,n+1):
        if n%fa==0:
            fc+=1
    return fc==2
def paly_prime(n):
    return prime(n) and pal(n)==n
        
print(paly_prime(21))

def prime(n,fc=0):
    for fa in range(1,n+1):
        if n%fa==0:
            fc+=1
    return fc==2
def pal(n,s=0):
    while n!=0:
        ld=n%10
        s=s*10+ld
        n//=10
    return s
def rpal(s,fc=0):
    for fa in range(1,s+1):
        if s%fa==0:
            fc+=1
    return fc==2
def emrip(n):
    return prime(n) and pal(n)!=n and rpal(n)


print(emrip(71))



def arm(n,ds=0):
    
    while n!=0:
        ld=n%10
        ds+=ld**len(str(n))
        n//=10
    return ds
def a(n):
    return n==arm(n)
print(a(135))


def fact(n,ds=0):
    while n!=0:
        ld=n%10
        fac=1
        for fa in range(ld,0,-1):
            fac*=fa
        ds+=fac
        n//=10
    return ds
def strong(n):
    return n==fact(n)

print(strong(145))


def rem(n):
    s=n**3
    c=len(str(n))
    r=s%(10*c)
    return r
def auto(n):
    return n==rem(n)
print(auto(7))

def no(n,ds=0):
    s=n**2
    while s!=0:
        ld=s%10
        ds+=ld
        s//=10
    return ds
def neno(n):
    return n==no(n)

print(neno(9))


def div(n,c=0):
    while n!=0:
        ld=n%2
        c+=ld
        n//=2
    return c%2==0
def evil(n):
    return div(n)
print(evil(15))

def t(n):
    n1=0
    n2=0
    c=len(str(n))//2
    ld=n%(10**c)
    n1+=ld
    n2+=n//2
    n3=(n1+n2)**2
    return n3
def tech(n):
    return n==t(n)
print(tech(2025))
    
'''
def one(n):
    while n>9:
        ds=0
        while n!=0:
            ld=n%10
            ds+=ld**2
            n//=10

    n=ds
    return n
    
def is_happy(n):
    return one(n)==1
print(is_happy(44))
        




