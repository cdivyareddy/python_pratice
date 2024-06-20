'''
with open ('file1.txt','r') as f:
    clines=0
    for i in f:
        clines+=1
    print(clines)

with open ('file.txt','r') as f:
    words=0
    for i in f:
        for w in i.split():
            words+=1
    print(words)
'''
