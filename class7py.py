Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> complex(10)
(10+0j)
>>> complex(10.5)
(10.5+0j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> complex("10)
	
SyntaxError: EOL while scanning string literal
>>> complex("10")
(10+0j)
>>> complex("10.5")
(10.5+0j)
>>> complex("ten")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    complex("ten")
ValueError: complex() arg is a malformed string
>>> complex(10,20)
(10+20j)
>>> complex(True,False)
(1+0j)
>>> complex(10,10.5)
(10+10.5j)
>>> complex("10","20")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    complex("10","20")
TypeError: complex() can't take second arg if first is a string
>>> bool(0.0)
False
>>> bool(0.1)
True
>>> bool(0.01)
True
>>> bool(10+20j)
True
>>> bool(0+0j)
False
>>> bool('')
False
>>> bool('varsh')
True
>>> bool(' ')
True
>>> str(10+20j)
'(10+20j)'
>>> 