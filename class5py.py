Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=10+20j
>>> x
(10+20j)
>>> type(x)
<class 'complex'>
>>> y=10.5+5.6j
>>> y
(10.5+5.6j)
>>> a=0b111+20j
>>> a
(7+20j)
>>> a=10+20j
>>> b=30+20j
>>> a+b
(40+40j)
>>> a-b
(-20+0j)
>>> a*b
(-100+800j)
>>> a=10+20j
>>> a.real
10.0
>>> a.imag
20.0
>>> a=10
>>> b=20
>>> a>b
False
>>> a<b
True
>>> true+true
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    true+true
NameError: name 'true' is not defined
>>> True+True
2
>>> True+False
1
>>> a='varsh'
>>> a
'varsh'
>>> type a
SyntaxError: invalid syntax
>>> type (a)
<class 'str'>
>>> s='''vars
            mech'''
>>> print(s)
vars
            mech
>>>  