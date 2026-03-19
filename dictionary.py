"""
peoples = {"sadik":24,"Raj":25,"sayeed":26}
print(peoples)
print(peoples.keys())
print(peoples.values())
print(peoples["sadik"])
print(peoples.get("sayeed"))        #we are not get item by values, sayeed here key


#for loops over dictionary
for person,age in peoples.items():      #we need to attached items() function with dictionary variable
    print("{} : {}".format(person,age))
    print(f"{person}: {age}")
    print('Person: '+person+"   Age: "+str(age))



#while loops over same dictionary
keys = list(peoples.keys())
index = 0
while index < len(keys):
    #print(keys[index])
    eachKey = keys[index]
    #print(f"{eachKey} : {peoples[eachKey]}")
    #print("{} : {}".format(eachKey,peoples[eachKey]))
    print("Person: "+eachKey+" Age: "+str(peoples[eachKey]))
    index += 1                  #Increment index to avoid an infinite loop



peoples.pop('sayeed')
print(peoples)

peoples.update(
    {
        "yo":44, "tee":32,
    }
)
print(peoples)


"""
"""

#................................car dictionary.......................................
#Direct lookup by ID → Dictionary of dictionaries
cars = {
    "Car1": {"brand": "Toyota", "budget": 15, "mileage": 18, "color": "White"},
    "Car2": {"brand": "Honda", "budget": 14, "mileage": 20, "color": "Black"},
    "Car3": {"brand": "Suzuki", "budget": 10, "mileage": 22, "color": "Red"},
    "Car4": {"brand": "Hyundai", "budget": 12, "mileage": 19, "color": "Blue"},
    "Car5": {"brand": "Nissan", "budget": 16, "mileage": 17, "color": "Silver"},
    "Car6": {"brand": "Kia", "budget": 13, "mileage": 21, "color": "White"}
}

max_budget = float(input("Enter your maximum budget (in lakh): "))
min_mileage = float(input("Enter minimum mileage (km/l): "))
preferred_color = input("Enter preferred color: ").capitalize()

print("\nCars matching your criteria:\n")

found = False

for car, info in cars.items():
    if (info["budget"] <= max_budget and info["mileage"] >= min_mileage and info["color"] == preferred_color):
        print(f"{car} → Brand: {info['brand']}, " f"Budget: {info['budget']} lakh, " f"Mileage: {info['mileage']} km/l, " f"Color: {info['color']}")
        found = True

if not found:
    print("No car meets your criteria.")



#................................car dictionary.......................................
#Searching / filtering → List of dictionaries
cars = [
    {"brand": "Toyota", "budget": 15, "mileage": 18, "color": "White"},
    {"brand": "Honda", "budget": 14, "mileage": 20, "color": "Black"},
    {"brand": "Suzuki", "budget": 10, "mileage": 22, "color": "Red"},
    {"brand": "Hyundai", "budget": 12, "mileage": 19, "color": "Blue"},
    {"brand": "Nissan", "budget": 16, "mileage": 17, "color": "Silver"},
    {"brand": "Kia", "budget": 13, "mileage": 21, "color": "White"},
    {"brand": "Ford", "budget": 11, "mileage": 18, "color": "Black"}
]
def filter_cars(cars, max_budget, min_mileage, preferred_colors):
    matched_cars = []

    for car in cars:
        if (
            car["budget"] <= max_budget and
            car["mileage"] >= min_mileage and
            car["color"] in preferred_colors
        ):
            matched_cars.append(car)

    return matched_cars

max_budget = float(input("Enter maximum budget (in lakh): "))
min_mileage = float(input("Enter minimum mileage (km/l): "))

colors_input = input("Enter preferred colors (comma separated): ")
preferred_colors = [color.strip().capitalize() for color in colors_input.split(",")]

result = filter_cars(cars, max_budget, min_mileage, preferred_colors)

print("\nCars matching your criteria:\n")

if result:
    for car in result:
        print(
            f"Brand: {car['brand']}, "
            f"Budget: {car['budget']} lakh, "
            f"Mileage: {car['mileage']} km/l, "
            f"Color: {car['color']}"
        )
else:
    print("No car meets your criteria.")

"""

#.................List of Dictionaries.................
#student

students = [
    {"Name": "Sadik", "Roll": 3, "Marks": 80},
    {"Name": "Raj", "Roll": 4, "Marks": 88},
    {"Name": "Nayeem", "Roll": 1, "Marks": 70}
]

print(students)

roll = int(input("Enter Roll:"))
#key = list(students.keys())         #Lists do not have keys()

found = False

for student in students:
    if student["Roll"] == roll:
        print("Student Found.")
        print("Name of student: ",student["Name"]," Roll: ",student["Roll"]," Marks: ",student["Marks"])
        found = True
        break

if not found:
    print("No Student found with this roll.")