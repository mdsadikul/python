"""
#for loop syntex

for i in range(10):
    print('*' * i)


#multiplication of int using for loop
num = int(input("Enter num: "))
for i in range(1, 11):
    print(num, "x", i, '=', num * i)


#multiplication of int using for loop with format function
num = int(input("Enter num: "))
for i in range(1, 11):
    print("{} x {} = {}".format(num, i, num * i))


#multiplication of int using for loop with user define function
def print_multiplication_table(number):
    for i in range(1, 11):
        print(number, "*", i, "=", number * i)


num = int(input("Which multiplication table you want to see: "))
print_multiplication_table(num)
"""


#iterating over a list
fruits = ['a','b','c']
for fruit in fruits:
    print(fruit)

word = 'hello world!'
for letter in word:
    print(letter)


# Example of iterating over a dictionary
student_scores = {'Alice': 90, 'Bob': 85, 'Charlie': 92}
for student, score in student_scores.items():
    print(f"{student}: {score}")


# Example of using break statement
for number in range(1,100):
    if number == 50:
        break
    print(number)


# Example of using break statement
for number in range(1,100,5):        #starting from 1, to 100, next iterate 5++
    if number == 50:
        continue
    print(number)

