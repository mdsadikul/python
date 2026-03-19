"""
  ..............while loop.............
i=1
while i <= 10:
    print(i)
    i += 1
"""

# Iterating over a list with a while loop

fruits = ['apple', 'banana', 'cherry']
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1


# Iterating over a string with a while loop
word = "hello"
index = 0
while index < len(word):
    print(word[index])
    index += 1


# Iterating over a dictionary with a while loop
student_scores = {'Alice': 90, 'Bob': 85, 'Charlie': 92}
keys = list(student_scores.keys())
index = 0
while index < len(keys):
    key = keys[index]
    print(f"{key}: {student_scores[key]}")
    index += 1

# Using break statement in a while loop
index = 0
end = 10
while index < end:
    if index == 5:
        break
    print(index)
    index += 1


# Using continue statement in a while loop
counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue        # for skipping specific iterate
    print(counter)


""".....................................................................................
def print_multiplication_table(number):
    for i in range(1, 11):
        print(number, "*", i, "=", number * i)


num = input("Enter a number (0 to exit): ")
num = int(num)

while num!=0:
    print_multiplication_table(num)
    print("")
    num = input("Enter a number (0 to exit): ")
    num = int(num)
"""

