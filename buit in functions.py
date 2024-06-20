Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 145&124
16
>>> 145\124
SyntaxError: unexpected character after line continuation character
>>> 145/124
1.1693548387096775
>>> 145|124
253
>>> 145^124
237
>>> list['abc']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list['abc']
TypeError: 'type' object is not subscriptable
>>> str(9.00)
'9.0'
>>> list('abc')
['a', 'b', 'c']
>>> s='bindu and divya '
>>> s='bindu and DiVYa '
>>> s.upper()
'BINDU AND DIVYA '
>>> s.lower()
'bindu and divya '
>>> s.swapcase()
'BINDU AND dIvyA '
>>> s.caplitalize()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.caplitalize()
AttributeError: 'str' object has no attribute 'caplitalize'
>>> s.capitalize()
'Bindu and divya '
>>> s.title()
'Bindu And Divya '
>>> s.isalpha()
False
>>> s.isalnum()
False
>>> s.digit()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.digit()
AttributeError: 'str' object has no attribute 'digit'
>>> s.digt()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.digt()
AttributeError: 'str' object has no attribute 'digt'
>>> s.isdigit()
False
>>> s.split()
['bindu', 'and', 'DiVYa']
>>> s.split('a')
['bindu ', 'nd DiVY', ' ']
>>> s.split('a',1)
['bindu ', 'nd DiVYa ']
>>> s.strip()
'bindu and DiVYa'
>>> s
'bindu and DiVYa '
>>> s='abindu and DiVYa 's.strip()
SyntaxError: invalid syntax
>>> s.strip()
'bindu and DiVYa'
>>> s='abindu and DiVYa '
>>> s.strip()
'abindu and DiVYa'
>>> s.strip('a')
'bindu and DiVYa '
>>> s='aaabindu and DiVYaaa'
>>> s.strip()
'aaabindu and DiVYaaa'
>>> s.strip('aa')
'bindu and DiVY'
>>> s='7777898878777'
>>> s.strip()
'7777898878777'
>>> s.strip('777')
'898878'
>>> s.strip('7777')
'898878'
>>> s.strip('777')
'898878'
>>> s.strip('7')
'898878'
>>> s.replace('and','%')
'7777898878777'
>>> s='abindu and DiVYa '
>>> s.replace('and','%')
'abindu % DiVYa '
>>> s.startswith('a')
True
>>> s.endswith('a')
False
>>> s.endswith('a')
False
>>> s.endswith('Ya')
False
>>> 
>>> s.endswith('Ya ')
True
>>> s.count()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s.count()
TypeError: count() takes at least 1 argument (0 given)
>>> s.count('a')
3
>>> l=['divya',3,5,3,[1,3],'bindu']
>>> l.append()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    l.append()
TypeError: append() takes exactly one argument (0 given)
>>> l.append('a')
>>> l
['divya', 3, 5, 3, [1, 3], 'bindu', 'a']
>>> l.append('a',1)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    l.append('a',1)
TypeError: append() takes exactly one argument (2 given)
>>> l.append([1,3])
>>> l
['divya', 3, 5, 3, [1, 3], 'bindu', 'a', [1, 3]]
>>> l.insert(0,[3,5])
>>> l
[[3, 5], 'divya', 3, 5, 3, [1, 3], 'bindu', 'a', [1, 3]]
>>> l.insert([3,5])
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    l.insert([3,5])
TypeError: insert() takes exactly 2 arguments (1 given)
>>> l.extend('ccccc')
>>> l
[[3, 5], 'divya', 3, 5, 3, [1, 3], 'bindu', 'a', [1, 3], 'c', 'c', 'c', 'c', 'c']
>>> l.extend([w,e,r,p])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    l.extend([w,e,r,p])
NameError: name 'w' is not defined
>>> l.extend(['w','e','r','p'])
>>> l
[[3, 5], 'divya', 3, 5, 3, [1, 3], 'bindu', 'a', [1, 3], 'c', 'c', 'c', 'c', 'c', 'w', 'e', 'r', 'p']
>>> l.remove()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    l.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> l.remove('c')
>>> l
[[3, 5], 'divya', 3, 5, 3, [1, 3], 'bindu', 'a', [1, 3], 'c', 'c', 'c', 'c', 'w', 'e', 'r', 'p']
>>> l.pop()
'p'
>>> l.pop('w')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    l.pop('w')
TypeError: 'str' object cannot be interpreted as an integer
>>> l.pop([1,3])
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    l.pop([1,3])
TypeError: 'list' object cannot be interpreted as an integer
>>> l.pop()
'r'
>>> l.pop(9)
'c'
>>> s.clear()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s.clear()
AttributeError: 'str' object has no attribute 'clear'
>>> l.clear()
>>> l
[]
>>> l=['divya',3,5,3,[1,3],'bindu']
>>> l.index('divya')
0
>>> l.index(3,1)
1
>>> l.index(3,2)
3
>>> min(l)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    min(l)
TypeError: '<' not supported between instances of 'int' and 'str'
>>> l=[2,5,6,7,0]
>>> max(l)
7
>>> min(1)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    min(1)
TypeError: 'int' object is not iterable
>>> min(l)
0
>>> reverse(l)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    reverse(l)
NameError: name 'reverse' is not defined
>>> l.reverse()
>>> l
[0, 7, 6, 5, 2]
>>> l.sort()
>>> l
[0, 2, 5, 6, 7]
>>> l.sort(True=reverse)
SyntaxError: keyword can't be an expression
>>> l.sort(reverse=True)
>>> l
[7, 6, 5, 2, 0]
>>> sorted(l)
[0, 2, 5, 6, 7]
>>> l.count(0)
1
>>> l.sorted()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    l.sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> sorted(l)
[0, 2, 5, 6, 7]
>>> t=(3,4,5,6,4)
>>> sorted(t)
[3, 4, 4, 5, 6]
>>> t.index(4)
1
>>> t.index(4,0)
1
>>> t.index(4,0,4)
1
>>> t.count(4)
2
>>> s={3,5,76,,64,46,(4,3,2))
SyntaxError: invalid syntax
>>> s={3,5,76,,64,46,(4,3,2)}
SyntaxError: invalid syntax
>>> s={3,5,76,64,46,(4,3,2)}
>>> s.add('s)
	  
SyntaxError: EOL while scanning string literal
>>> s.add('s')
	  
>>> s
	  
{64, 's', 3, 5, 76, 46, (4, 3, 2)}
>>> s.update((2,3))
	  
>>> s
	  
{64, 's', 2, 3, 5, 76, 46, (4, 3, 2)}
>>> s.update([2,3])
	  
>>> s
	  
{64, 's', 2, 3, 5, 76, 46, (4, 3, 2)}
>>> s.remove(76)
	  
>>> s
	  
{64, 's', 2, 3, 5, 46, (4, 3, 2)}
>>> s.pop(-1)
	  
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    s.pop(-1)
TypeError: pop() takes no arguments (1 given)
>>> s.pop()
	  
64
>>> s.count(2)
	  
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    s.count(2)
AttributeError: 'set' object has no attribute 'count'
>>> s.discard(2)
	  
>>> s
	  
{'s', 3, 5, 46, (4, 3, 2)}
>>> s.discard(6)
	  
>>> s
	  
{'s', 3, 5, 46, (4, 3, 2)}
>>> s.clear()
	  
>>> s
	  
set()
>>> s=
	  
SyntaxError: invalid syntax
>>> s={5,7,6}
	  
>>> s1={5}
	  
>>> s.intersection(s1)
	  
{5}
>>> s.union(s1)
	  
{5, 6, 7}
>>> s.difference(s1)
	  
{6, 7}
>>> 
