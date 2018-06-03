#read file
'''
with open("yamuna.txt","r")as f:
    s=f.read()
print s
'''

#read line
'''
with open("yamuna.txt","r")as f:
    s=f.readline()
print s

'''
    
#read lines
'''
with open("yamuna.txt","r")as f:
    s=f.readlines()
print s
'''

#write file
'''
with open("yamuna.txt","w")as f:
     s=f.write("hii dad \n")
     s1=f.write("hello mom \n")
     s2=f.write("nice to meeting u friends")
print s
'''   
#how to print the perticular line in a read file
'''

f=open('yamuna.txt')
lines=f.readlines()
print lines[0]
print lines[2]
'''

#how to append the file
'''
with open("yamuna.txt", "a") as myfile:
    myfile.write("this is yamuna")

'''

 
#how to read  and write the file
'''
with open("yamuna.txt",'r+b') as f:
    s=f.write("new line write \n")
    y = f.readline(2)
print s
print y
'''

#how to open image file in pyton

'''
f= open('hello.jpg', 'r+')
jpgdata = f.read()
f.close()
print jpgdata
'''
#how to print perticular sring in file
'''
import mmap
f= open('yamuna.txt')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if s.find('aaaaa') != -1:
    print('true')
else:
    print ('Fals')
 
'''




#how to print ip address in text file
'''
import re
text = "This sentence contains an ip number 1.2.3.4 and 111.111.111.111 451.976.897.786 port number 50, i want to print the IP address only."
foo = re.findall(r'(?<!\S)(?:\d{1,3}\.){3}\d{1,3}(?!\S)', text)
print foo
'''

'''

for i in range(1):
    for j in range(1):
        ip = "11.16.%d.%d" % (i, j)
        print ip
 '''       
