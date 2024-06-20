def is_prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount
def prime(num):
    return is_prime(num)==2
def composite(num):
    return is_prime(num)>2