Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=10
>>> y=10
>>> x is y
True
>>> x=10
>>> y=x
>>> x=20
>>> y=20
>>> x is y
True
>>> x=10
>>> x=y
>>> y=20
>>> x==y
True
>>> x=10
>>> x=y
>>> y=20
>>> x=y
>>> x is y
True
>>> x=10
>>> x=y
>>> y=20
>>> x is y
True
>>> 
>>> 
>>> 
>>> x=10
>>> y=10
>>> x+=10
>>> x=y
>>> x is y
True
>>> x=10
>>> 
>>> 
>>> x=10
>>> y=10
>>> x+=10
>>> x is y
False
>>> x=10
>>> y=10
>>> x+=10
>>> y++=10
SyntaxError: invalid syntax
>>> x=10
>>> y=10
>>> x+=10
>>> y+=10
>>> x is y
True
>>> x=10
>>> y=10
>>> x==10
True
>>> x=10
>>> y=20
>>> x-y=0
SyntaxError: can't assign to operator
>>> x=10
>>> y=10
>>> x-=10
>>> x is y
False
>>> x=10
>>> y=20
>>> x-y=0
SyntaxError: can't assign to operator
>>> x=10
>>> y=20
>>> y-x=0
SyntaxError: can't assign to operator
>>> x=10
>>> y=20
>>> y-x=10
SyntaxError: can't assign to operator
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x-y
-10
>>> x=10
>>> 
>>> x=20
>>> y-=10
>>> x==y
False
>>> x==0
False
>>> x==10
False
>>> 
