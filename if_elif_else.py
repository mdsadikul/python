"""
#1  even and odd number using if else:
num = int(input("Enter any number: "))

if num == 0:
    print(num, "is zero")
elif num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

"""

"""
#2  now create it user define function:
def print_even_odd(num):
    if num == 0:
        print(num, "is zero")
    elif num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")


#now use it in our code, Let's see
n = int(input('enter any integer number:'))
print_even_odd(n)

"""

"""
#3  grading system for nsu:
def nsu_grade(mark):
    if mark >= 90 and mark <= 100:
        return "A"
    elif mark >= 85 and mark <= 89:
        return "A-"
    elif mark >= 80 and mark <= 84:
        return "B+"
    elif mark >= 75 and mark <= 79:
        return "B"
    elif mark >= 70 and mark <= 74:
        return "B-"
    elif mark >= 65 and mark <= 69:
        return "C+"
    elif mark >= 60 and mark <= 64:
        return "C"
    elif mark >= 57 and mark <= 59:
        return "C-"
    elif mark >= 55 and mark <= 56:
        return "D+"
    elif mark >= 50 and mark <= 54:
        return "D"
    elif mark >= 0 and mark < 50:
        return "F"
    else:
        return "Invalid Marks"


# User input
course_mark = int(input("Enter your course mark: "))
grade = nsu_grade(course_mark)
print("Your grade is:", grade)

"""



"""
#Leap year problem:
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")
"""


#-------------------------------------------------------------------------
today = input("Enter the day: ").capitalize()
holiday = input("Is today a holiday? (yes/no): ").lower()

#if today in ["Friday", "Saturday"] or holiday == "yes":
if today == "Friday" or today == "Saturday" or holiday == "yes":
    print("No office today.")
else:
    print("Yes office today.")








"""
You and your date are trying to get a table at a restaurant. 
The parameter "you" is the stylishness of your clothes, in the range 0..10, 
and "date" is the stylishness of your date's clothes. The result getting 
the table is encoded as an int value with 0=no, 1=maybe, 2=yes. I
f either of you is very stylish, 8 or more, then the result is 2 (yes). 
With the exception that if either of you has style of 2 or less,
then the result is 0 (no). Otherwise the result is 1 (maybe).

date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
"""
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1


y = int(input("enter your :"))
yur = int(input("enter your_date :"))
print(date_fashion(y, yur))
