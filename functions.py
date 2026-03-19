"""
#-----------------------USER DEFINE FUNCTION:---------------------------

def add_two_num(a,b):
    print(a+b)

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
add_two_num(num1,num2)



#-------------------Variable-Length Arguments(*args)   (tuples)--------------------------
def addtwo(*numbers):                           # using * it become a tuple, SO THAT TAKE TUPLE ITEMS
    for num in numbers:
        print(num)

addtwo(23,4,3,'sadik',3.5,True)



#-----------------keyword arguments (**args)     (dictionary)-----------------------------
def addtwo(**person):                           # using ** it become a dictionary
    #print(person)
    #print(person['name'])
    for key,value in person.items():
        print(f"{key}: {value}")
        #print(key+":"+str(value))

addtwo(name= "sadik",age=24,cg=4.00,)

"""

"""
#............................function return...........................#
def add_two_num(a,b):
    sum = a+b
    div = a/b
    return sum

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
result = add_two_num(num1,num2)
print(result)

#-----sort way-------
def add_two_num(a,b):
    return a+b, a-b                 #if we want multipule return, we can but result print as a tuple
                                    #also we are able to print through list and dicrionary

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
print(add_two_num(num1,num2))




#-------Early return for early exit--------
def find_even_number (numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None

ans = find_even_number([1,4,11,5,7,9])
print(ans)

"""


"""
#.....................................................................................
#.......--------.functon local / global variables.----------------------------........
def myfunc():
    x=10    #local
    y=5     #local
    print(x+y)

myfunc()
#print(x)     -here we can't access x outside of myfunc(), so it is a local var


a = 190  # global
b = 59  # global
def myfunc():
    print(a+b)

myfunc()
print(a)     # here we can access a/b outside of myfunc(), so it is a global var


n = 100 #global
def num1():
    n = 10  #local
    print(n)

num1()
def num2():
    print(n)

num2()


#.....----change global value in locally--------------
n = 100

def num1():
    global n
    n = 10        #এখানে global n পরিবর্তন হয়ে যাচ্ছে
    r = n + 1
    print(r)

num1()

def num2():
    r = n + 50
    print(r)

num2()

"""


"""
#---------------------------------------------------------------------------------------------------------
#------------------------------------max function---------------------------------------------

numbers = [1,3,4,5,33,2,1,9,4]
max_number = max(numbers)
print(max_number)


#---------------------------linear search:------------------------------------

numbers = [1,3,4,5,33,2,1,9,4]
max_number = float('-inf')              # it means that, max_num contain very small number compare to list all items
for n in numbers:
    if n > max_number:
        max_number = n

print(max_number)


# -------------------linear search by random numbers:--------------------------

import random
numbers = []                                    #create an empty list
for _ in range(10):                             
    numbers.append(random.randint(1,100))       #generates a random integer between 1 and 100 & adds each random number to the list

print(numbers)

max_number = float('-inf')
for n in numbers:
    if n > max_number:
        max_number = n

print(max_number)

"""

"""
#-------------------Get current date & time----------------------
from datetime import datetime

today = datetime.now()
print(today)
print(today.time())
print(today.year)

now = datetime.now()
formatted = now.strftime("%d-%m-%Y %I:%M %p")
print(formatted)
"""

"""
def my_fun(a=0,b=0,c=0):    #local var
    global d        #100
    d = d*2         #200    #global var change here
    n = a+b+c       #0
    return n*2      #0

def another_fun():
    print("d == ",d)    #200

d = 100             #global
x = my_fun()
another_fun()
print(x)    #0
print(d)    #200

"""

"""
#------------------------------------------------------------------------------
#when we send var then it copy as local var, but when we send a list, it doesn't copy. Here li and nums are locate same
#memory location. So when we change li[0] = 100, alternetivly its change nums[0] items. On Other hand n remains same.

#send list on function

def my_f(li,n):             #reference
    li[0] = 100
    n = 10
    return max(li)

nums = [10,20,40,15,4]
n = 4
x = my_f(nums, n)
print(x)
print(nums)
print(n)

"""
"""
def Hello():
    def Say():
        txt = "Hello World"
        return txt
    return Say

x = Hello()
print(x())
"""


