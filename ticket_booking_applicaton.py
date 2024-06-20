def single_ton(func):
    l=[]
    def inner(*args,**kwargs):
        if len(l)==0:
            l.append(func())
        return l[-1]
    return inner
@single_ton
class family_star:
    def __init__ (self):
        self.maxt=200
    def booking(self,NOT):
        if NOT<=self.maxt:
            print(' fam tickets are booked successfully')
            self.maxt-=NOT
            print(f'remaing tickets are:{self.maxt}')
        else:
            print('no sufficent tickets....!')
@single_ton
class hanuman:
    def __init__ (self):
        self.maxt=200
    def booking(self,NOT):
        if NOT<=self.maxt:
            print('tickets are booked successfully')
            self.maxt-=NOT
            print(f'remaing tickets are:{self.maxt}')
        else:
            print('no sufficent tickets....!')




            
def paytm():
    print('1>family star\n 2>hanuman')
    selection=int(input('enter the choice:'))
    if selection==1:
          ob=family_star()
          ob.booking(int(input('enter number of tickets:')))
    elif selection==2:
          ob1=hanuman()
          ob1.booking(int(input('enter number of tickets:')))
    else:
        print('invalid movie')
def bmys():
    print('1>family star\n 2>hanuman')
    selection=int(input('enter the choice:'))
    if selection==1:
          ob=family_star()
          ob.booking(int(input('enter number of tickets:')))
    elif selection==2:
          ob1=hanuman()
          ob1.booking(int(input('enter number of tickets:')))
    else:
        print('invalid movie')


paytm()
paytm()
bmys()
