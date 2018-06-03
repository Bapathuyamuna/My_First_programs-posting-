Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
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
>>> d={'a':1,'b':2,'c':3}
>>> d
{'a': 1, 'c': 3, 'b': 2}
>>> d.clear()
>>> d
{}
>>> d.copy()
{}
>>> d
{}
>>> d={'a':1,'b':2,'c':3}
>>> d
{'a': 1, 'c': 3, 'b': 2}
>>> d.copy()
{'a': 1, 'c': 3, 'b': 2}
>>> d.fromkeys('a')
{'a': None}
>>> d.fromkeys()

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    d.fromkeys()
TypeError: fromkeys expected at least 1 arguments, got 0
>>> d.has_key()

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d.has_key()
TypeError: has_key() takes exactly one argument (0 given)
>>> d.has_key(2)
False
>>> d.has_key('b')
True
>>> d.items()
[('a', 1), ('c', 3), ('b', 2)]
>>> d.iteritems()
<dictionary-itemiterator object at 0x0274E150>
>>> d.iteritems('a')

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d.iteritems('a')
TypeError: iteritems() takes no arguments (1 given)
>>> d.iteritems(1)

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    d.iteritems(1)
TypeError: iteritems() takes no arguments (1 given)
>>> d.iterkeys()
<dictionary-keyiterator object at 0x02626090>
>>> d.iterkeys('a')

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d.iterkeys('a')
TypeError: iterkeys() takes no arguments (1 given)
>>> d.itervalues()
<dictionary-valueiterator object at 0x0274E1E0>
>>> d.itervalues(1)

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.itervalues(1)
TypeError: itervalues() takes no arguments (1 given)
>>> d.keys()
['a', 'c', 'b']
>>> d.values()
[1, 3, 2]
>>> d.pop('a)
      
SyntaxError: EOL while scanning string literal
>>> d.pop('a')
1
>>> d
{'c': 3, 'b': 2}
>>> d.popitem('c')

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    d.popitem('c')
TypeError: popitem() takes no arguments (1 given)
>>> d.popitem()
('c', 3)
>>> d
{'b': 2}
>>> d.setdefault()

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    d.setdefault()
TypeError: setdefault expected at least 1 arguments, got 0
>>> d.setdefault('a')
>>> d
{'a': None, 'b': 2}
>>> d.update()
>>> d
{'a': None, 'b': 2}
>>> d1={'a':1,'b':2,'c':3}
>>> d2={'d':4,'e':5,'f':6}
>>> d1.update(d2)
>>> d1
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'f': 6}
>>> d1.viewitems()
dict_items([('a', 1), ('c', 3), ('b', 2), ('e', 5), ('d', 4), ('f', 6)])
>>> d1.viewkeys()
dict_keys(['a', 'c', 'b', 'e', 'd', 'f'])
>>> d1.viewvalues()
dict_values([1, 3, 2, 5, 4, 6])
>>> d\

   
{'a': None, 'b': 2}

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> d.fromkeys()

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    d.fromkeys()
TypeError: fromkeys expected at least 1 arguments, got 0
>>> d.fromkeys('a')
{'a': None}
>>> d.iterkeys()
<dictionary-keyiterator object at 0x0274E150>
>>> l= [1,2,3,4,5,2,1,4,6]
>>> set(l)
set([1, 2, 3, 4, 5, 6])
>>> set.add('e')

Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    set.add('e')
TypeError: descriptor 'add' requires a 'set' object but received a 'str'
>>> set.add(1)

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    set.add(1)
TypeError: descriptor 'add' requires a 'set' object but received a 'int'
>>> set.add()

Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    set.add()
TypeError: descriptor 'add' of 'set' object needs an argument
>>> set.add(9)

Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    set.add(9)
TypeError: descriptor 'add' requires a 'set' object but received a 'int'
>>> l = [1,2,4,5,6]
>>> l1=[1,2,3,4,5,6]
>>> set(l1)-set(l)
set([3])
>>> File "<pyshell#64>", line 1, in <module>
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> d
{'a': None, 'b': 2}
>>> d = {'a':1,'b':2,'c':3}
>>> d['a']=10
>>> d
{'a': 10, 'c': 3, 'b': 2}
>>> d['A']=d.pop('a')
>>> d
{'A': 10, 'c': 3, 'b': 2}
>>> d['B']=10
>>> d
{'A': 10, 'c': 3, 'b': 2, 'B': 10}
>>> d={'a':1,'b':2,'c':3}
>>> d.get('a')
1
>>> d.popitem()
('a', 1)
>>> d
{'c': 3, 'b': 2}
>>> d.keys
