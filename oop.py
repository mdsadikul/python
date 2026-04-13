x = 5
print(type(x))
#print(dir(x))          #showing all built-in methods of integer class
print(x.numerator)  #here numerator and denominator are the property of int class
print(x.denominator)
print(x.bit_count())  #bit_count() is a built-in method of int class

my_list = [1, 2, 3]
print(type(my_list))
#print(dir(my_list))
my_list.append(4)
print(my_list)


#-----------user define class::::::and create object-------------
#----------------------------------------------------------------


#-----------#Practice No-1----------
class MyClass:
    total = 6

    def HelloWorld(self):
        print("Hello")


print(MyClass.total)
# we create an obj of this class
obj = MyClass()
print(obj.total)
obj.HelloWorld()
print(dir(obj))


#------------------------------------


#-----------#Practice No-2----------
import math
class Fraction:
    def __init__(self, n, d):  #constructor
        self.numerator = n  #This runs automatically when create an object.
        self.denominator = d

    def __str__(self):  #magic function
        return "{} / {}".format(self.numerator, self.denominator)

    def simplify(self):
        g = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator / g
        self.denominator = self.denominator / g     # using // instead of / , it print integer.


f1 = Fraction(20, 40)
print(f1)
#print(f1.numerator, f1.denominator)
f1.simplify()
print(f1)

