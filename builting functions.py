#range program
'''
f=range(10)
print f
'''
#x_range progrrame
'''
f=xrange(333)
print f
'''


#programes of lambda


'''
f=lambda n:n*n
print f(10)
'''
'''
f=lambda x,y:x*y
print f(10,20)
'''

#program of itarator
'''
l=range(10)
for x in l:
    print(x)
'''
#program of genarator
#l =rnge(10)
'''
def get(l):
    for x in l:
        yield x*x
obj=get(range(1,10))
print obj.next()
print obj.next()
print obj.next()
print obj.next()
print obj.next()
print obj.next()
print obj.next()
print obj.next()
print obj.next()
'''


#function programes
#map
'''
l=range(10)
y=map(lambda x:x*x,l)
print(y)
'''


#filter
'''
l=range(10)
y=filter(lambda x:x%2,l)
print(y)
'''
#reduce

l=range(10)
y=reduce(lambda x,y:x+y,l)
print(y)




