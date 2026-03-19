"""
(Project 1) : Simple Calculator

OVERVIEW:
In this assignment, you will develop a basic calculator program using Python. This project
will reinforce fundamental programming concepts including functions, user input,
conditional statements, and error handling. The application will run in the terminal and
should not use any external libraries or frameworks.


TASKS:
1. Function Definitions: Implement functions for the following operations: addition,
subtraction, multiplication, division, and modulus. Each function should take two
arguments, perform the corresponding operation, and return the result.
2. Implement User Input Handling: Prompt the user to select an operation( e.g. 1
for Add, 2 for Subtract, 3 for Multiply, 4 for Divide and 5 for Modulus) and input two
numbers. Convert these inputs into appropriate data types for calculations.
3. Conditional Logic: Use ‘if’, ‘elif’, and ‘else’ statements to determine which
arithmetic operation to perform based on user selection.
4. Output Formatting: Display the results in a clear and readable format. Examples:
Addition: 5 + 6 = 11
Division: 5 / 2 = 2.50
5. Error Handling: Include checks to handle division by zero and other potential
errors. Provide informative error messages to guide the user.


SAMPLE INPUT OUTPUT:
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus
Enter choice (1/2/3/4/5): 1
Enter first number: 5
Enter second number: 8
5.0 + 8.0 = 13.0
"""

#---------------------------------------simple one---------------------
def add(x, y):
    r = x + y
    return r


def sub(x, y):
    r = x - y
    return r


def mul(x, y):
    r = x * y
    return r


def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    r = x / y
    return r


def mod(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot calculate modulus by zero.")
    r = x % y
    return r


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

try:
    n = int(input("Enter choice (1/2/3/4/5):"))
    if n not in range(1, 6):
        raise ValueError("Invalid operation choice!")

    x = float(input("Enter first number:"))
    y = float(input("Enter second number:"))

    if n == 1:
        print(f"{x} + {y} = {add(x, y)}")
    elif n == 2:
        print(f"{x} - {y} = {sub(x, y)}")
    elif n == 3:
        print(f"{x} * {y} = {mul(x, y)}")
    elif n == 4:
        # Using :.2f formats the division result to 2 decimal places
        print(f"{x} / {y} = {div(x, y):.2f}")
    elif n == 5:
        print(f"{x} % {y} = {mod(x, y)}")

except ValueError:
    print(f"Input Error: {ValueError}")
except ZeroDivisionError:
    print("Math Error: ", ZeroDivisionError)
except Exception as e:
    print(f"Unexpected Error: {e}")



#------------------------------more professional one---------------------

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y


def mod(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot calculate modulus by zero!")
    return x % y


def main():
    # The while loop keeps the program running until the user chooses to exit
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("0. Exit")

        try:
            # Choice input
            n = int(input("Enter choice (1/2/3/4/5/0): "))

            # Check for exit condition first
            if n == 0:
                print("Exiting the calculator. Goodbye!")
                break  # This breaks out of the while loop, ending the program

            # Validate menu choice
            if n not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid choice!")

            # Number inputs
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            # Perform operation
            if n == 1:
                print(f"Addition: {x} + {y} = {add(x, y)}")
            elif n == 2:
                print(f"Subtraction: {x} - {y} = {sub(x, y)}")
            elif n == 3:
                print(f"Multiplication: {x} * {y} = {mul(x, y)}")
            elif n == 4:
                print(f"Division: {x} / {y} = {div(x, y):.2f}")
            elif n == 5:
                print(f"Modulus: {x} % {y} = {mod(x, y)}")

        except ValueError:
            print(f"Input Error: {ValueError}")
        except ZeroDivisionError:
            print("Math Error: ", ZeroDivisionError)
        except Exception as e:
            print(f"Unexpected Error: {e}")


# This is a Python best practice: it checks if the script is being run directly
if __name__ == "__main__":
    main()






























"""



def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def mod(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot calculate modulus by zero.")
    return x % y


# Dictionary mapping (Professional approach)
operations = {
    1: ("+", add),
    2: ("-", sub),
    3: ("*", mul),
    4: ("/", div),
    5: ("%", mod)
}


def show_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("0. Exit")


# Main loop (Program runs until user exits)
while True:
    show_menu()

    try:
        choice = int(input("Enter choice (0-5): "))

        if choice == 0:
            print("Calculator closed.")
            break

        if choice not in operations:
            raise ValueError("Invalid menu choice.")

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        symbol, function = operations[choice]
        result = function(x, y)

        # Formatting division to 2 decimal places
        if choice == 4:
            print(f"{x} {symbol} {y} = {result:.2f}")
        else:
            print(f"{x} {symbol} {y} = {result}")

    except ValueError:
        print("Input Error: Please enter valid numeric values.")
    except ZeroDivisionError as e:
        print(f"Math Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

"""


















