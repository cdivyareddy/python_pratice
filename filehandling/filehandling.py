''''ob=open('file.txt','w')
ob.write('divya\ncahran\nreddy')
ob.writelines(['div'])
ob.close()



ob=open('file.txt','w')
ob.writelines(['hello\n','hi\n','bye'])
ob.close()


ob=open('file.txt','r')
print(ob.read())
print(ob.readlines(3))
print(ob.tell())



with open('file.txt') as f:
    print(len(f.readlines()))

with open('file.txt') as f:
    lines=0
    for c in f:
        lines+=1
    print(lines)

with open ('file.txt') as f:
    w=0
    for _ in f:
        for words in _.split():
            w+=1
    
    print(w)




with open('file.txt') as f:
    c=0
    for ch in f:
        ch=ch.strip('\n')
        c+=len(ch)
    print(c)


with open('file.txt') as f:
    c=0
    for ch in f:
        ch=ch.strip('\n')
        for l in ch:
            if l in 'aeiouAEIOU':
               c+=1
    print(c)




with open('file.txt') as f:
    c=0
    for ch in f:
        ch=ch.strip('\n')
        for l in ch.split():
            if l[0] in 'aeiouAEIOU':
               c+=1
    print(c)

#json

import json
d={1:20,4:20,3:80}
with open('jfile.json','w') as fobj:
    fobj.write(json.dumps(d,indent=4,sort_keys=True))


import json
d={1:20,4:20,3:80}
with open('numjson.json','w') as fobj:
    json.dump(d,fobj,indent=3)


import json
with open('numjson.json','r') as fobj:
    jsonobj=fobj.read()
    print(json.loads(jsonobj))



import json
with open('numjson.json','r') as fobj:
    print(json.load(fobj))

import pickle
d={1:20,4:20,3:80}
with open('p.pkl','wb') as fobj:
    fobj.write(pickle.dumps(d))

import pickle
d={1:20,4:20,3:80}
with open('p.pkl','wb') as fobj:
    pickle.dump(d,fobj)



import pickle
with open('p.pkl','rb') as fobj:
    d=fobj.read()
    print(pickle.loads(d))


'''
import pickle
with open('p.pkl','rb') as fobj:
    print(pickle.load(fobj))









