Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='varshini'
>>> s(0)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s(0)
TypeError: 'str' object is not callable
>>> [0]
[0]
>>> s='varshini'
>>> s[0]
'v'
>>> s[5]
'i'
>>> s[8]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s[8]
IndexError: string index out of range
>>> s[6]
'n'
>>> [-5]
[-5]
>>> s[-4]
'h'
>>> s[-1]
'i'
>>> s[1:5]
'arsh'
>>> s=[0:1]
SyntaxError: invalid syntax
>>> s=[0;5]
SyntaxError: invalid syntax
>>> s=[0:5]
SyntaxError: invalid syntax
>>> s=[3:6]
SyntaxError: invalid syntax
>>> s'varshini'
SyntaxError: invalid syntax
>>> s='varshini'
>>> s[0:5]
'varsh'
>>> s[1:]
'arshini'
>>> s[7:]
'i'
>>> s[:7]
'varshin'
>>> s[:5]
'varsh'
>>> s[:]
'varshini'
>>> s[1:100]
'arshini'
>>> s='varshinimechanical'
>>> s[1:10]
'arshinime'
>>> s[1:10:2]
'asiie'
>>> s='vars'
>>> s*5
'varsvarsvarsvarsvars'
>>> len(s)
4
>>> int(123.456)
123
>>> int(10+20j0
    
SyntaxError: invalid syntax
>>> int(10+20j)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(10+20j)
TypeError: can't convert complex to int
>>> int(TRUE)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(TRUE)
NameError: name 'TRUE' is not defined
>>> int(True)
1
>>> int(False)
0
>>> int("10.5")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int("10.5")
ValueError: invalid literal for int() with base 10: '10.5'
>>> int("10")
10
>>> float(10)
10.0
>>> float(10=20j)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> float(10+20j)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    float(10+20j)
TypeError: can't convert complex to float
>>> float(True)
1.0
>>> float("10")
10.0
>>> float("10.5")
10.5
>>> float("ten")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    float("ten")
ValueError: could not convert string to float: 'ten'
>>> 