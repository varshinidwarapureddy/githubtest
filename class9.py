Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s=[10,"varsh",True]
>>> S=S*2
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    S=S*2
NameError: name 'S' is not defined
>>> s=s*2
>>> 
>>> s=[10,"vrah",True]
>>> s=s*2
>>> s
[10, 'vrah', True, 10, 'vrah', True]
>>> type(s)
<class 'list'>
>>> t=(10,"vars",True,20)
>>> t
(10, 'vars', True, 20)
>>> t[0]
10
>>> t[o:3]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t[o:3]
NameError: name 'o' is not defined
>>> t[0:3]
(10, 'vars', True)
>>> t1=t*2
>>> t1
(10, 'vars', True, 20, 10, 'vars', True, 20)
>>> r= range(10)
>>> type(r)
<class 'range'>
>>> r
range(0, 10)
>>> for i in r:print(i)

0
1
2
3
4
5
6
7
8
9
>>> r[0]
0
>>> r[0:3]
range(0, 3)
>>> r=rang(10)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    r=rang(10)
NameError: name 'rang' is not defined
>>> r=range(10)
>>> r[0]9
SyntaxError: invalid syntax
>>> r[0]=9
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    r[0]=9
TypeError: 'range' object does not support item assignment
>>> for i is range(10,50,5):print(i)
SyntaxError: invalid syntax
>>> 
>>> 
>>> for i is range(10,50,5) :print(i)
SyntaxError: invalid syntax
>>> 
>>> for i is range(10,50,5): print(i)
SyntaxError: invalid syntax
>>> for i is range(10,50,5):print(i)
SyntaxError: invalid syntax
>>>  