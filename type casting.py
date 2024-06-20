Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s="my name is divya"
>>> s.upper()
'MY NAME IS DIVYA'
>>> print(type(s))
<class 'str'>
>>> str="My NAME is Divya"
>>> print(s.lower())
my name is divya
>>> s.tittle()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.tittle()
AttributeError: 'str' object has no attribute 'tittle'
>>> str.tittle()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    str.tittle()
AttributeError: 'str' object has no attribute 'tittle'
>>> str.capitalize()
'My name is divya'
>>> str.split()
['My', 'NAME', 'is', 'Divya']
>>> str.split('a')
['My NAME is Divy', '']
>>> str.split('a',1)
['My NAME is Divy', '']
>>> str.split('a',100)
['My NAME is Divy', '']
>>> str.split('a','a')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    str.split('a','a')
TypeError: 'str' object cannot be interpreted as an integer
>>> str.swapcase()
'mY name IS dIVYA'
>>> str.tittle
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    str.tittle
AttributeError: 'str' object has no attribute 'tittle'
>>> str.tittle()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    str.tittle()
AttributeError: 'str' object has no attribute 'tittle'
>>> str="fhgjhGF"
>>> str1=str.tittle()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    str1=str.tittle()
AttributeError: 'str' object has no attribute 'tittle'
>>> 
============== RESTART: C:/python qspiders/built in methods.py ==============
Traceback (most recent call last):
  File "C:/python qspiders/built in methods.py", line 2, in <module>
    str1=str.tittle()
AttributeError: 'str' object has no attribute 'tittle'
>>> str.title()
'My Name Is Divya'
>>> 
'My Name Is Divya'
'My Name Is Divya'
>>> str="likitha GOOd girl"
>>> str.upper()
'LIKITHA GOOD GIRL'
>>> type(str)
<class 'str'>
>>> str.lower()
'likitha good girl'
>>> type(str)
<class 'str'>
>>> str.swapcase()
'LIKITHA gooD GIRL'
>>> type(str)
<class 'str'>
>>> str.title()
'Likitha Good Girl'
>>> type.str()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    type.str()
AttributeError: type object 'type' has no attribute 'str'
>>> type(str)
<class 'str'>
>>> str.split()
['likitha', 'GOOd', 'girl']
>>> str.split('i')
['l', 'k', 'tha GOOd g', 'rl']
>>> str.split('i',1)
['l', 'kitha GOOd girl']
>>> str.split('i',67)
['l', 'k', 'tha GOOd g', 'rl']
>>> 
