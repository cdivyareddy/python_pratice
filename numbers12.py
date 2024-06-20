def is_prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2
def prime(num):
    return is_prime(num)

