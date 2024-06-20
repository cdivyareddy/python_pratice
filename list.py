Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s="jshv''sbb"
>>> s(len)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s(len)
TypeError: 'str' object is not callable
>>> len(s)
9
>>> type(s)
<class 'str'>
>>> l=[[['benz','audi'],['RR','Ferrari'],'jagour','Bugatti'],['Rover']]]
SyntaxError: invalid syntax
>>> l
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> L=[[['benz','audi'],['RR','Ferrari'],'jagour','Bugatti'],['Rover']]]
SyntaxError: invalid syntax
>>> L=[[['benz','audi'],['RR','Ferrari'],'jagour','Bugatti'],['Rover']]
>>> L[0][0][0][0][0]
'b'
>>> L[0][0][0][0][1]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    L[0][0][0][0][1]
IndexError: string index out of range
>>> L[0][0][0][0][0]
'b'
>>> L[0][0][0][0][0][1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    L[0][0][0][0][0][1]
IndexError: string index out of range
>>> L[0][0][0][0][0]
'b'
>>> L[0][0][0][0][1]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    L[0][0][0][0][1]
IndexError: string index out of range
>>> L=[[[['benz','audi'],['RR','Ferrari'],'jagour','Bugatti'],['Rover']]]
>>> l
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> L
[[[['benz', 'audi'], ['RR', 'Ferrari'], 'jagour', 'Bugatti'], ['Rover']]]
>>> L[0]
[[['benz', 'audi'], ['RR', 'Ferrari'], 'jagour', 'Bugatti'], ['Rover']]
>>> L[0][0]
[['benz', 'audi'], ['RR', 'Ferrari'], 'jagour', 'Bugatti']
>>> l[0][0][0]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l[0][0][0]
NameError: name 'l' is not defined
>>> L[0][0][0]
['benz', 'audi']
>>> L[0][0][0][1]
'audi'
>>> L[0][0][0][0][0]
'b'
>>> L[0][0][0][0][1]
'e'
>>> L[0][0][0][0][2]
'n'
>>> L[0][0][0][0][3]
'z'
>>> L[0][0][0][1]
'audi'
>>> L[0][0][0][1][0]
'a'
>>> L[0][0][0][1][1]
'u'
>>> L[0][0][0][1][2]
'd'
>>> L[0][0][0][1][3]
'i'
>>> L[0][0][1][0]
'RR'
>>> 
L[0][0][1][0][0]
'R'
>>> L[0][0][1][0][1]
'R'
>>> L[0][0][1][1]
'Ferrari'
>>> L[0][0][1][1][0]
'F'
>>> L[0][0][1][1][1]
'e'
>>> L[0][0][1][1][2]
'r'
>>> L[0][0][1][1][3]
'r'
>>> L[0][0][1][1][4]
'a'
>>> L[0][0][1][1][5]
'r'
>>> L[0][0][1][1][6]
'i'
>>> L[0][0][1][2]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    L[0][0][1][2]
IndexError: list index out of range
>>> L[0][0][2]
'jagour'
>>> 







'
L[0][0][2]
SyntaxError: EOL while scanning string literal
>>> L[0][0][2]
'jagour'
>>> L[0][0][2][0]
'j'
>>>  L[0][0][2][1]
SyntaxError: unexpected indent
>>> L[0][0][2][1]
'a'
>>> L[0][0][2][2]
'g'
>>> L[0][0][2][3]
'o'
>>> L[0][0][2][4]
'u'
>>> L[0][0][2][5]
'r'
>>> l[0][0][3]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    l[0][0][3]
NameError: name 'l' is not defined
>>> L[0][0][3]
'Bugatti'
>>> L[0][0][3][0]
'B'
>>> L[0][0][3][1]
'u'
>>> L[0][0][3][2]
'g'
>>> L[0][0][3][3]
'a'
>>> L[0][0][3][4]
't'
>>> L[0][0][3][5]
't'
>>> L[0][0][3][6]
'i'
>>> L[0][0][3][7]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    L[0][0][3][7]
IndexError: string index out of range
>>> L[0][1]
['Rover']
>>> l[0][1][0]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    l[0][1][0]
NameError: name 'l' is not defined
>>> L[0][1][0]
'Rover'
>>> L[0][1][1]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    L[0][1][1]
IndexError: list index out of range
>>> L[0][1][0][0]
'R'
>>> L[0][1][0][1]
'o'
>>> L[0][1][0][2]
'v'
>>> L[0][1][0][3]
'e'
>>> L[0][1][0][4]
'r'
>>> 
