Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> L=[["bindu",33365,["divya",23]],["charan",4566,3+j7]]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    L=[["bindu",33365,["divya",23]],["charan",4566,3+j7]]
NameError: name 'j7' is not defined
>>> L=[["bindu",33365,["divya",23]],["charan",4566,3+7j]]
>>> l
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> L
[['bindu', 33365, ['divya', 23]], ['charan', 4566, (3+7j)]]
>>> L[0]
['bindu', 33365, ['divya', 23]]
>>> len(L)
2
>>> L[0][1][3]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    L[0][1][3]
TypeError: 'int' object is not subscriptable
>>> L[0][0][3]
'd'
>>> L[1][0][2]
'a'
>>> L[0][1][0][1]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    L[0][1][0][1]
TypeError: 'int' object is not subscriptable
>>> L[0][2][0][2]
'v'
>>> 
