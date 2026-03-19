"""
#Temperature Calculator using if-elif-else

print('.....................Convert Temperature.....................\n')
from_ = input("Convert from (C/F/K): ").upper()
to_ = input("Convert to: (C/F/K): ").upper()

temp = input('Enter temp: ')
temp = float(temp)

result = None

# Celsius conversions
if from_ == 'C':
    if to_ == 'F':
        result = (temp * 9/5) + 32
    elif to_ == 'K':
        result = temp + 273.15
    else:
        result = temp

# Fahrenheit conversions
elif from_ == 'F':
    if to_ == 'C':
        result = (temp - 32) * 5 / 9
    elif to_ == "K":
        result = (temp - 32) * 5 / 9 + 273.15
    else:
        result = temp

# Kelvin conversions
elif from_ == "K":
    if to_ == "C":
        result = temp - 273.15
    elif to_ == "F":
        result = (temp - 273.15) * 9/5 + 32
    else:
        result = temp

else:
    print("Invalid temp!")
    exit()

print(f"Converted Temperature: {result:.2f} {to_}")     #f means formatted string (f-string).

#print("Converted Temperature: {:.2f} {}".format(result, to_)) #without f
#print("Converted Temperature:", round(result, 2), to_)  #without f
"""

"""
#Temperature Calculator using match-case

print('.....................Convert Temperature.....................\n')
from_ = input("Convert from (C/F/K): ").upper()
to_ = input("Convert to: (C/F/K): ").upper()

temp = input('Enter temp: ')
temp = float(temp)

result = None

match (from_, to_):
    case ("C", "F"):
        result = (temp * 9 / 5) + 32
    case ("C", "K"):
        result = temp + 273.15
    case ("F", "C"):
        result = (temp - 32) * 5 / 9
    case ("F", "K"):
        result = (temp - 32) * 5 / 9 + 273.15
    case ("K", "C"):
        result = temp - 273.15
    case ("K", "F"):
        result = (temp - 273.15) * 9 / 5 + 32
    case ("C", "C") | ("F", "F") | ("K", "K"):
        result = temp
    case _:                             #anything else , Same as default in switch-case
        print("Invalid conversion!")
        exit()

print(f"Converted Temperature: {result:.2f} {to_}")
"""



#Temperature Calculator using User-Defined Function
def convert_temperature(from_unit, to_unit, temp):
    match (from_unit, to_unit):
        case ("C", "F"):
            return (temp * 9/5) + 32
        case ("C", "K"):
            return temp + 273.15
        case ("F", "C"):
            return (temp - 32) * 5/9
        case ("F", "K"):
            return (temp - 32) * 5/9 + 273.15
        case ("K", "C"):
            return temp - 273.15
        case ("K", "F"):
            return (temp - 273.15) * 9/5 + 32
        case ("C", "C") | ("F", "F") | ("K", "K"):
            return temp
        case _:
            return None


from_unit = input("Convert FROM (C/F/K): ").upper()
to_unit = input("Convert TO (C/F/K): ").upper()
temp = float(input("Enter temperature value: "))

result = convert_temperature(from_unit, to_unit, temp)

if result is None:
    print("Invalid conversion!")
else:
    print(f"Converted Temperature: {result:.2f} {to_unit}")
