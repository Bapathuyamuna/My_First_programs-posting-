#the given number is palindrome or not
'''
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
'''

#the given string is palindrome or not

'''
def reverse(s):
    return s[::-1]

def isPalindrome(s):
    
    rev = reverse(s)
 
    
    if (s == rev):
        return True
    return False
 
 

s = "malayalam"
ans = isPalindrome(s)
 
if ans == 1:
    print("the given string is palindrome")
else:
    print("the given string is not palindrome")


#prime number
'''
'''
num = 200
if num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

else:
   print(num,"is not a prime number")
   '''

#even and odd number
'''


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
   '''

'''

my_str = 'aIbohPhoBiA'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")
'''

#write the program of factorial (using controlle statement)
'''
num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
'''
#with out using recurtion to find factorial(using for looping statement)

n=int(input("Enter number:"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial of the number is: ")
print(fact)

#how to find power of the numer by using recurtion

'''
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))
'''


