#some pyramid pattern problems:
"""
print()	                New line
print(end="")	        Stay on same line
print(end=" ")	        Add space
print(end=",")	        Add comma
"""

"""Q:
    *
   ***
  *****
 *******
*********
"""
row = int(input("Enter numbers of row: "))
for i in range(1, row + 1):
    print(" " * (row - i) + "*" * (2 * i - 1))

#or

for i in range(1, row + 1):
    for j in range(row - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()

"""Q:
      A 
     A B 
    A B C 
   A B C D 
  A B C D E 
"""
n = 5
alph = 65
for i in range(0, n):
    print(" " * (n - i), end=" ")
    for j in range(0, i + 1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()

"""Q:
    1
   123
  12345
 1234567
123456789
"""
r = 5
for i in range(1, r + 1):
    print(" " * (r - i), end="")
    for j in range(2 * i - 1):
        print(j + 1, end="")
    print()

"""Q:
*********
 *******
  *****
   ***
    *
"""
def inverted_pyramid(row):
    for i in range(row,0,-1):
        print(" " * (row - i) + "*" * (2 * i - 1))
inverted_pyramid(3)

#or

r=5
for i in range(r,0,-1):
    print(" "*(r-i),end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

#or

for i in range(r,0,-1):
    for x in range(r-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()


"""Q:Hollow Pyramid Patterns
    *    
   * *   
  *   *  
 *     * 
*********
"""
