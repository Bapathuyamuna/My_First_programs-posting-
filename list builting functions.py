>>> l=[1,2,3,4]
>>> l.append('yamuna')
>>> 
>>> l
[1, 2, 3, 4, 'yamuna']
>>> l.insert('yamuna')

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    l.insert('yamuna')
TypeError: insert() takes exactly 2 arguments (1 given)
>>> l.insert(6,'yamuna')
>>> l
[1, 2, 3, 4, 'yamuna', 'yamuna']
>>> l.count('yamuna')
2
>>> l
[1, 2, 3, 4, 'yamuna', 'yamuna']
>>> l.count(4)
1
>>> l=[1,2,3]
>>> l1=[4,5,6]
>>> l.extend(l1)
>>> l1
[4, 5, 6]
>>> l+l1
[1, 2, 3, 4, 5, 6, 4, 5, 6]
>>> l1.extend(l)
>>> l1
[4, 5, 6, 1, 2, 3, 4, 5, 6]
>>> l=[1,2,3]
>>> l1=[4,5,6]l.extend(l1)
SyntaxError: invalid syntax
>>> l=[1,2,3,4]
>>> l.index(1)
0
>>> l.index(3)
2
>>> l.pop(2)
3
>>> l
[1, 2, 4]
>>> l=['yamuna']
>>> l.remove('m')

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    l.remove('m')
ValueError: list.remove(x): x not in list
>>> l=[1,2,3,4]
>>> l=[5,6,4,8,3]
>>> l.sort()
>>> l
[3, 4, 5, 6, 8]
>>> l.extend()

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l.extend()
TypeError: extend() takes exactly one argument (0 given)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> t=(1,2,3,4)
>>> t.count(3)
1
>>> t.index(3)
2
>>> t1=(1,2,3,4)
>>> t2=(5,6,7,8)
>>> t1+t2
(1, 2, 3, 4, 5, 6, 7, 8)
>>> t=(1,2,3,4)
>>> for i in t
SyntaxError: invalid syntax
>>> t.apend()

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t.apend()
AttributeError: 'tuple' object has no attribute 'apend'
