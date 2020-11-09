Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[10,20,30,40]
>>> n=bytes(x)
>>> type(b)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(b)
NameError: name 'b' is not defined
>>> b=bytes(x)
>>> type(b)
<class 'bytes'>
>>> b[0}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> b[0]
10
>>> b[1]
20
>>> b[-1]
40
>>> b[0:4]
b'\n\x14\x1e('
>>> foe x in b:print
SyntaxError: invalid syntax
>>> for x in b:print(x)

10
20
30
40
>>> x=[10,20,30,40]
>>> b=bytearray(x)
>>> type(b)
<class 'bytearray'>
>>> b(0)=120
SyntaxError: cannot assign to function call
>>> b[0]-120
-110
>>> b[0]=120
>>> for i in b:print(i)

120
20
30
40
>>> x=[10,20,128]
>>> b=bytearray(x)
>>> b[0]=256
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b[0]=256
ValueError: byte must be in range(0, 256)
>>> x=[10,20,256]
>>> b=bytearray(x)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b=bytearray(x)
ValueError: byte must be in range(0, 256)
>>> l=[]
>>> type(l)
<class 'list'>
>>> l.append(10)
>>> l.append(20)
>>> l.append(30)
>>> l.append(10)
>>> print(l)
[10, 20, 30, 10]
>>> l.append('varh')
>>> print(l)
[10, 20, 30, 10, 'varh']
>>> l(0)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    l(0)
TypeError: 'list' object is not callable
>>> l[0]
10
>>> l[-1]
'varh'
>>> l[1:4]
[20, 30, 10]
>>> 