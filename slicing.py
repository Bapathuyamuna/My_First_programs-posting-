Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s='hello yamuna'
>>> s=[1:1]
SyntaxError: invalid syntax
>>> s[0:1]
'h'
>>> s[0:2]
'he'
>>> s[0:3]
'hel'
>>> s=[0:4]
SyntaxError: invalid syntax
>>> s[0:5]
'hello'
>>> s[0:4]
'hell'
>>> s[0:6]
'hello '
>>> s[1:-1]
'ello yamun'
>>> s[1:-2]
'ello yamu'
>>> s[2:-2]
'llo yamu'
>>> s[::]
'hello yamuna'
>>> s[:]
'hello yamuna'
>>> s[::-1]
'anumay olleh'
>>> s[:-1]
'hello yamun'
>>> s[:-2]
'hello yamu'
>>> s[::-4]
'aal'
>>> s[:-1:2]
'hloymn'
>>> s[:-2:2]
'hloym'
>>> s[:-3:1]
'hello yam'
>>> s[s[:1:-1]
  s[:1:-1]
  
SyntaxError: invalid syntax
>>> s[:1:-2]
'aua l'
>>> s='hello yamuna'
>>> s[:1:-2]
'aua l'
>>> s[:2:-2]
'aua l'
>>> s[:3:-2]
'aua '
>>> s[3::-1]
'lleh'
>>> s[4::-1]
'olleh'
>>> s[5::-1]
' olleh'
>>> s[-1::5]
'a'
>>> s[-2::5]
'n'
>>> s[-2::6]
'n'
>>> s[-3::2]
'ua'
>>> s[-3::3]
'u'
>>> s[-3::4]
'u'
>>> 
