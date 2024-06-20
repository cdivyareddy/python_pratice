'''class example:
    name='divya'
    age='22'
    rollno='20HR1A0518'
    dept='CSE'
    college='MTIET'
s1=example()
s2=example()
s3=example()
s4=example()

example.name='bindu'

print(s1.name)
print(s2.name)
print(example.name)


class sample:
    c_name='divya'
    c_id=1001
    c_mobileno=9573398094

c1=sample()
c2=sample()
c3=sample()
sample.c_name='charan'
print(c1.c_name)
print(c2.c_name)
print(c3.c_name)

class student:
    course_name='python'
    batch_code='m10'
    trainer='sai santhosh'
    branch='marthahalii'
    def __init__(self,name,s_id,mno,age):
        self.name=name
        self.s_id=s_id
        self.mno=mno
        self.age=age

s1=student('divya',518,9573398094,21)
s2=student('charan',517,798162612,20)
print(s1.name)
print(s2.s_id)
print(s1.course_name)
'''
class bank:
    bank_name='union'
    branch_name='v.kota'
    ifsc='SDE21SD234'
    rof=4
    def __init__(self,name,accno,mno,balance,pin):
        self.name=name
        self.accno=accno
        self.mno=mno
        self.balance=balance
        self.pin=pin
c1=bank('divya','ASDE123445',9573398094,2000000,1403)
c2=bank('charan','KJKN23NB5',8755563649,8000000,2002)
print(c1.name)
print(c2.name)
print(c2.balance)
    
    
