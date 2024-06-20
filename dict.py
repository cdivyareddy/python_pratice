Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> v={'a':{'a':'python','b':'java'},'H':{'h':{'hello','world'},'e':'Bye'}}
>>> v
{'a': {'a': 'python', 'b': 'java'}, 'H': {'h': {'hello', 'world'}, 'e': 'Bye'}}
>>> v['a']['a'][0]
'p'
>>> v['a']['a'][1]
'y'
>>> v['a']['a'][2]
't'
>>> v['a']['a'][3]
'h'
>>> v['a']['a'][4]
'o'
>>> v['a']['a'][5]
'n'
>>> v['a']['b'][0]
'j'
>>> v['a']['b'][1]
'a'
>>> v['a']['b'][2]
'v'
>>> v['a']['b'][3]
'a'
>>> v['a']['H']['h'][0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    v['a']['H']['h'][0]
KeyError: 'H'
>>> v['H']['h'][0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    v['H']['h'][0]
TypeError: 'set' object does not support indexing
>>> v['a']['H']['h'][0][0]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    v['a']['H']['h'][0][0]
KeyError: 'H'
>>> len(v)
2
>>> v['H']['h'][0][0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    v['H']['h'][0][0]
TypeError: 'set' object does not support indexing
>>> v['H']
{'h': {'hello', 'world'}, 'e': 'Bye'}
>>> v['H']['h']
{'hello', 'world'}
>>> V['H']['h'][0]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    V['H']['h'][0]
NameError: name 'V' is not defined
>>> v['H']['e']
'Bye'
>>> v['H']['e'][0]
'B'
>>>  v['H']['e'][1]
SyntaxError: unexpected indent
>>> v['H']['e'][1]
'y'
>>> v['H']['e'][2]
'e'
>>> "nsjkhfia''csknc"
"nsjkhfia''csknc"
>>> s="jkds''jsdckj"
>>> s[0]
'j'
>>> s[0]=2
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s[0]=2
TypeError: 'str' object does not support item assignment
>>> len(s)
12
>>> var={True+True,12,68}
>>> Var={True+True,1,0,False}
>>> len(var)
3
>>> var
{2, 12, 68}
>>> Var={True+True,1,0,False}
>>> var
{2, 12, 68}
>>> v={True+True,1,0,False}
>>> v
{0, 1, 2}
>>> v={True+True,1,False,0}
>>> v
{False, 1, 2}
>>> 
