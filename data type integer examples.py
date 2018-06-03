Python 2.7aw1.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=4
>>> y=2
>>> if not 1+1==y or x==4 and 7==8
SyntaxError: invalid syntax
>>> 
======================= RESTART: C:/Python27/yamuna.py =======================
no
>>> 
>>> 
>>> a=10
>>> b=10
>>> a is b
True
>>> a=1000
>>> b=1000
>>> print 'a' is 'b'
False
>>> a=1000
>>> b=1000
>>> a is b
False
>>> x=yamuna

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x=yamuna
NameError: name 'yamuna' is not defined
>>> x='yamuna'
>>> y='yamuna'
>>> x is y
True
>>> x='yamuna'
>>> y='yamuna'
>>> print 'x' is 'y'
False
>>> x=10
>>> x==10
True
>>> x is 10
True
>>> x==20
False
>>> z==20

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    z==20
NameError: name 'z' is not defined
>>> z=20
>>> z==20
True
>>> x=4
>>> y=7
>>> x is y
False
x=1000
y=1000
x is y

