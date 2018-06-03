#how to add the name
'''
name='yamuna'
print"how are you",name,"this is "
'''
'''
import re
match = re.match(r"([a-z]+)([0-9]+)", 'foofo21', re.I)
if match:
	items = match.groups()
print(items)
'''


s=list('hello yamuna')
s[11:15]=' this'
a=''.join(s)
print(a)
