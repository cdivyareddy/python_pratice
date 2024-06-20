Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s='ikitha doing well'
>>> s.replace('k','s')
'isitha doing well'
>>> s.alpha()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s.alpha()
AttributeError: 'str' object has no attribute 'alpha'
>>> s.isalpha
<built-in method isalpha of str object at 0x0000013C90414BB8>
>>> s.isalpha()
False
>>> s.isdigit()
False
>>> s.isalnum()
False
>>> s='kkjn'
>>> s.isalpha()
True
>>> s="igyf68"
>>> s.isalnum()
True
>>> s.index('i')
0
>>> s.index('6')
4
>>> s='ikitha doing well'
>>> s.replace('well','not bad')
'ikitha doing not bad'
>>> s='divya'
>>> s.alpha()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.alpha()
AttributeError: 'str' object has no attribute 'alpha'
>>> s.isalpha()
True
>>> s.isdigits.isalpha()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.isdigits.isalpha()
AttributeError: 'str' object has no attribute 'isdigits'
>>> s.isdigit()
False
>>> s.isalnum()
True
>>> s="she is looking like a wow"
>>> s.index('i')
4
>>> s.index('i',5)
11
>>> s.index('i',12)
16
>>> s.index(s.index('i')+1)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.index(s.index('i')+1)
TypeError: must be str, not int
>>> s.index('i',s.index('i')+1)
11
>>> s.index('i',s.index('i',s.index('i')+1)+1)
16
>>> s= 'moye moye moye moye'
>>> s.index('e',(s.index('e')+1)+1)
8
>>> 
>>> s.index('e',s.index('e',(s.index('e')+1)+1)+1)
13
>>> s.index('e',-7)
13
>>> s.index('e',-11)
8
>>> s.index('e',4,8)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.index('e',4,8)
ValueError: substring not found
>>> s.index('e',4,9)
8
>>> s= 'moye MOye moYE moye'
>>> s.upper()
'MOYE MOYE MOYE MOYE'
>>> s.lower()
'moye moye moye moye'
>>> s.swapcase()
'MOYE moYE MOye MOYE'
>>> s.capitalize()
'Moye moye moye moye'
>>> s.title()
'Moye Moye Moye Moye'
>>> s.repalce('ye','eee')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    s.repalce('ye','eee')
AttributeError: 'str' object has no attribute 'repalce'
>>> s.replace('y','eee')
'moeeee MOeeee moYE moeeee'
>>> s.replace('y','eee',1)
'moeeee MOye moYE moye'
>>> s.replace('y','eee',5)
'moeeee MOeeee moYE moeeee'
>>> s.split()
['moye', 'MOye', 'moYE', 'moye']
>>> s.split('e')
['moy', ' MOy', ' moYE moy', '']
>>> s.split('e',1)
['moy', ' MOye moYE moye']
>>> s.split('e',567)
['moy', ' MOy', ' moYE moy', '']
>>> s.isalpha()
False
>>> s.isalnum()
False
>>> s.isdigit()
False
>>> s.index(7)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    s.index(7)
TypeError: must be str, not int
>>> s.index('y')
2
>>> s= 'moye MOye moYE moye'
>>> s.index('y',5)
7
>>> s.index('y',s.index('y')+1)
7
>>> s.index('y',-14)
7
>>> 
