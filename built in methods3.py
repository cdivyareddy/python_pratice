Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=[45,6,4,24,5]
>>> l.append('5')
>>> l
[45, 6, 4, 24, 5, '5']
>>> l.append([2,3,5])
>>> l
[45, 6, 4, 24, 5, '5', [2, 3, 5]]
>>> l.append('')
>>> l
[45, 6, 4, 24, 5, '5', [2, 3, 5], '']
>>> l.append()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l.append()
TypeError: append() takes exactly one argument (0 given)
>>> l.insert('4',3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    l.insert('4',3)
TypeError: 'str' object cannot be interpreted as an integer
>>> l.insert(3,'4')
>>> l
[45, 6, 4, '4', 24, 5, '5', [2, 3, 5], '']
>>> l.insert(4,4)
>>> l
[45, 6, 4, '4', 4, 24, 5, '5', [2, 3, 5], '']
>>> l.insert(5,[4,6,7])
>>> l
[45, 6, 4, '4', 4, [4, 6, 7], 24, 5, '5', [2, 3, 5], '']
>>> 
>>> l.extend('4')
>>> l
[45, 6, 4, '4', 4, [4, 6, 7], 24, 5, '5', [2, 3, 5], '', '4']
>>> l.entend('420')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l.entend('420')
AttributeError: 'list' object has no attribute 'entend'
>>> l.extend('420')
>>> l
[45, 6, 4, '4', 4, [4, 6, 7], 24, 5, '5', [2, 3, 5], '', '4', '4', '2', '0']
>>> l.append('420')
>>> l
[45, 6, 4, '4', 4, [4, 6, 7], 24, 5, '5', [2, 3, 5], '', '4', '4', '2', '0', '420']
>>> l.insert('23')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l.insert('23')
TypeError: insert() takes exactly 2 arguments (1 given)
>>> l.insert(9,'334')
>>> l
[45, 6, 4, '4', 4, [4, 6, 7], 24, 5, '5', '334', [2, 3, 5], '', '4', '4', '2', '0', '420']
>>> l.pop()
'420'
>>> l
[45, 6, 4, '4', 4, [4, 6, 7], 24, 5, '5', '334', [2, 3, 5], '', '4', '4', '2', '0']
>>> l.pop(9)
'334'
>>> l
[45, 6, 4, '4', 4, [4, 6, 7], 24, 5, '5', [2, 3, 5], '', '4', '4', '2', '0']
>>> l.pop(-1)
'0'
>>> l
[45, 6, 4, '4', 4, [4, 6, 7], 24, 5, '5', [2, 3, 5], '', '4', '4', '2']
>>> l.remove(2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    l.remove(2)
ValueError: list.remove(x): x not in list
>>> l.remove('2')
>>> l
[45, 6, 4, '4', 4, [4, 6, 7], 24, 5, '5', [2, 3, 5], '', '4', '4']
>>> l.remove([2,3,5])
>>> l
[45, 6, 4, '4', 4, [4, 6, 7], 24, 5, '5', '', '4', '4']
>>> l.clear()
>>> l
[]
>>> l=[4,6,3,2,4,5,9]
>>> l.sort()
>>> l
[2, 3, 4, 4, 5, 6, 9]
>>> l.sorted()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l.sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> sorted(l)
[2, 3, 4, 4, 5, 6, 9]
>>> l.sort(reverse=True)
>>> l
[9, 6, 5, 4, 4, 3, 2]
>>> l=[94,6,23,6,7,9]
>>> l.sort(reverse=True)
>>> l
[94, 23, 9, 7, 6, 6]
>>> l.reverse()
>>> l
[6, 6, 7, 9, 23, 94]
>>> l=[4,6,3,2,4,5,9]
>>> l.reverse()
>>> l
[9, 5, 4, 2, 3, 6, 4]
>>> l.max()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    l.max()
AttributeError: 'list' object has no attribute 'max'
>>> max(l)
9
>>> min(l)
2
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    l.count()
TypeError: count() takes exactly one argument (0 given)
>>> l.count(4)
2
>>> l.index(4)
2
>>> l.index(l.index(4)+1)
4
>>> l.index(4,l.index(4)+1)
6
>>> l="hgf"
>>> y=l.copy()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    y=l.copy()
AttributeError: 'str' object has no attribute 'copy'
>>> j=[9,8]
>>> y=j.copy()
>>> print(y)
[9, 8]
>>> k='hjk'
>>> y=k.copy()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    y=k.copy()
AttributeError: 'str' object has no attribute 'copy'
>>> v=[7,8,9,0]
>>> ' '.join(v)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    ' '.join(v)
TypeError: sequence item 0: expected str instance, int found
>>> print(' '.join(v))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print(' '.join(v))
TypeError: sequence item 0: expected str instance, int found
>>> l=['5','67','6','4']
>>> print(' '.join(l))
5 67 6 4
>>> t=3,4,5,3,5,5,3,6,4
>>> t.index(5)
2
>>> t.count(3)
3
>>> t.sorted()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    t.sorted()
AttributeError: 'tuple' object has no attribute 'sorted'
>>> sorted(t)
[3, 3, 3, 4, 4, 5, 5, 5, 6]
>>> s={7,9,6,0,5}
>>> s.add(8)
>>> s
{0, 5, 6, 7, 8, 9}
>>> s.upadate('23')
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s.upadate('23')
AttributeError: 'set' object has no attribute 'upadate'
>>> s.update('23')
>>> s
{0, '3', 5, 6, 7, 8, 9, '2'}
>>> s.remove()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> s.remove(6)
>>> s
{0, '3', 5, 7, 8, 9, '2'}
>>> s.pop()
0
>>> s.pop(3)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    s.pop(3)
TypeError: pop() takes no arguments (1 given)
>>> s.discard(7)
>>> s
{'3', 5, 8, 9, '2'}
>>> s.discard(454)
>>> s
{'3', 5, 8, 9, '2'}
>>> s={8,5,2,5,2,5,6,9}
>>> s1={6,9,8,4,0}
>>> s.union(s1)
{0, 2, 4, 5, 6, 8, 9}
>>> s.intersection(s1)
{8, 9, 6}
>>> s.difference(s1)
{2, 5}
>>> s1.difference(s)
{0, 4}
>>> s1.difference(s1)
set()
>>> s1.issubset(s)
False
>>> s.clear()
>>> s
set()
>>> d={}
>>> d['divya']=['reddy']
>>> d
{'divya': ['reddy']}
>>> d['divya']='reddy'
>>> d
{'divya': 'reddy'}
>>> d.update('e':'eeeee')
SyntaxError: invalid syntax
>>> dd.update('e','eeeee')
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    dd.update('e','eeeee')
NameError: name 'dd' is not defined
>>> d.update('e','eeeee')
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    d.update('e','eeeee')
TypeError: update expected at most 1 arguments, got 2
>>> d={}
>>> d.update('d':45)
SyntaxError: invalid syntax
>>> d.update({'d':45})
>>> d
{'d': 45}
>>> d.update(['ab','23345'])
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    d.update(['ab','23345'])
ValueError: dictionary update sequence element #1 has length 5; 2 is required
>>> d.update(['ab','23345'])
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    d.update(['ab','23345'])
ValueError: dictionary update sequence element #1 has length 5; 2 is required
>>> d.update(['ab','23'])
>>> d
{'d': 45, 'a': 'b', '2': '3'}
>>> d.get('a')
'b'
>>> g.get('2')
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    g.get('2')
NameError: name 'g' is not defined
>>> d.get('2')
'3'
>>> d.key()
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'
>>> d.keys()
dict_keys(['d', 'a', '2'])
>>> d.values()
dict_values([45, 'b', '3'])
>>> d.items()
dict_items([('d', 45), ('a', 'b'), ('2', '3')])
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> d.pop('a')
'b'
>>> d.popitems()
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    d.popitems()
AttributeError: 'dict' object has no attribute 'popitems'
>>> d.popitem()
('2', '3')
>>> d
{'d': 45}
>>> d.popitem()
('d', 45)
>>> d
{}
>>> d.clear()
>>> d
{}
>>> v=[3,5,2]
>>> v2="divya"
>>> {}.fromkeys(v,v1)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    {}.fromkeys(v,v1)
NameError: name 'v1' is not defined
>>> {}.fromkeys(v,v2)
{3: 'divya', 5: 'divya', 2: 'divya'}
>>> v=[3,5,2,4,3,4,2,0,5,3]
>>> v2="divya"{}.fromkeys(v,v1)
SyntaxError: invalid syntax
>>> {}.fromkeys(v,v1)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    {}.fromkeys(v,v1)
NameError: name 'v1' is not defined
>>> {}.fromkeys(v,v2)
{3: 'divya', 5: 'divya', 2: 'divya', 4: 'divya', 0: 'divya'}
>>> zip(v,v1)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    zip(v,v1)
NameError: name 'v1' is not defined
>>> zip(v,v2)
<zip object at 0x00000213B36C5C88>
>>> list(zip(v,v2))
[(3, 'd'), (5, 'i'), (2, 'v'), (4, 'y'), (3, 'a')]
>>> list(zip(v))
[(3,), (5,), (2,), (4,), (3,), (4,), (2,), (0,), (5,), (3,)]
>>> 
