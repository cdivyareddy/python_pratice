for space,star in zip(range(4,-1,-1),range(1,9,2)):
    print(space*' ',star*'*',sep='')
for space,star in zip(range(1,5),range(7,0,-2)):
    print(space*' ',star*'*',sep='')
for space,star,kali,chuka in zip(range(4,-1,-1),range(1,9,2),range(1,5),range(7,0,-2)):
    print(space*' ',star*'*',kali*' ',chuka*'*',sep='')
