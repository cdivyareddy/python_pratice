Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s=" hey prabu hari ram krishana "
>>> s.index('a')
7
>>> s.index('a',8)
12
>>> s.index('a',s.index('a')+1)
12
>>> s.find('k')
20
>>> s.find('u')
9
>>> s.find('uu')
-1
>>> s.rindex('a')
27
>>> s.rinex('a',0,s.rindex('a'))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.rinex('a',0,s.rindex('a'))
AttributeError: 'str' object has no attribute 'rinex'
>>> s.rindex('a',0,s.rindex('a'))
25
>>> s.rfind('a')
27
>>> s.rfind('a',o,s.rfind('a'))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.rfind('a',o,s.rfind('a'))
NameError: name 'o' is not defined
>>> s.rfind('a',0,s.rfind('a'))
25
>>> s.strip()
'hey prabu hari ram krishana'
>>> s=12344561234"
SyntaxError: EOL while scanning string literal
>>> s='12344561234"
SyntaxError: EOL while scanning string literal
>>> s='12344561234"
SyntaxError: EOL while scanning string literal
>>> s="12344561234"
>>> s.strip('123')
'44561234'
>>> s.strip('1')
'2344561234'
>>> s="  12344561234  "
>>> s.strip('')
'  12344561234  '
>>> s.strip()
'12344561234'
>>> s.strip('1234')
'  12344561234  '
>>> s="12344561234"
>>> s.strip('1234')
'56'
>>> s='222222'
>>> s.strip('22')
''
>>> s.lstrip('22')
''
>>> s.rstrip('22')
''
>>> s='12345232431234'
>>> s.lstrip('1234')
'5232431234'
>>> s.rstrip('1234')
'12345'
>>> name='divya'
>>> mobile='redmi 9 prime'
>>> print('{} is using {} mobile'.format(name,mobile))
divya is using redmi 9 prime mobile
>>> print('{0} is using {1} mobile'.format(name,mobile))
divya is using redmi 9 prime mobile
>>> print('{1} is using {0} mobile'.format(name,mobile))
redmi 9 prime is using divya mobile
>>> print('{a} is using {b} mobile'.format(a=name,b=mobile))
divya is using redmi 9 prime mobile
>>> print(f'{name} is using {mobile} mobile')
divya is using redmi 9 prime mobile
>>> 
