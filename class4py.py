Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a=0b1111
>>> a
15
>>> a=-ob1111
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=-ob1111
NameError: name 'ob1111' is not defined
>>> a=-0b1111
>>> a
-15
>>> a=0o111
>>> a
73
>>>  a=0xface
 
SyntaxError: unexpected indent
>>> a=0xface
>>> a
64206
>>> a=0xvarshini
SyntaxError: invalid hexadecimal literal
>>> a=0Xvarshini
SyntaxError: invalid hexadecimal literal
>>> a=0xabcd
>>> a
43981
>>> 