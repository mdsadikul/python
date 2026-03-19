#csv, try--except, json
#------------------------------------------------------------------------------------------------------
#------------------------CSV---------------------------
"""
# Make list from CSV File

import csv

data = [
    ["Name", "Salary", "Designation", "Department", "Location"],
    ["Alice", 70000, "Software Engineer", "IT", "New York"],
    ["Bob", 85000, "Data Scientist", "Data", "San Francisco"],
    ["Charlie", 60000, "System Administrator", "IT", "Chicago"],
    ["David", 95000, "Product Manager", "Product", "Boston"],
    ["Eve", 72000, "UX Designer", "Design", "Los Angeles"]
]

with open('example.csv','w') as file:
    csv_file = csv.writer(file)
    csv_file.writerows(data)
    print("created successfully")

"""

"""
#Make CSV File From List
import csv

data = []

with open('example.csv','r') as file:
    content = csv.reader(file)
    for row in content:
        #print(row)
        data.append(row)

print(data)

"""

"""
#----------------------Exception handling-----------------------

#single exception handling:
try:
    s = 4/0
    print(s)

except ZeroDivisionError:
    print(ZeroDivisionError)

#Multipule exception handling:
try:
    with open('new.text','r') as file:
      content = file.read()
      result = 10 / int(content)
      print(result)

except FileNotFoundError:
    print(FileNotFoundError)
except ValueError:
    print(ValueError)
except TypeError:
    print(TypeError)
except ZeroDivisionError:
    print(ZeroDivisionError)


#Multiple exception handling using one except:
try:
    with open('new.text','r') as file:
      content = file.read()
      result = 10 / int(content)
      print(result)

except Exception as e:
    print(e)



#-----------------Final block in Exception Handling-------------------------
try:
    with open('new.text','r') as file:
      content = file.read()
      result = 10 / int(content)
      print(result)

except Exception as e:
    print(e)
finally:
    print("Execution completed.")

"""



 
#-------------------------------JSON---------------------------------

# create json string from dictionary
import json
students = {
     "Name": "Sadik",
     "Roll": 3,
     "Marks": 80,
     "Course":["Python","Django","React"],
}

json_format = json.dumps(students)
print(json_format)
#print actual json format: indent =4
json_format = json.dumps(students,indent=4)         # dumps
print(json_format)



# dictionary_data to json_data to json_file

with open("new/demo.json",'w') as file:
    json.dump(students,file,indent=4)               # dump
    print("completed")


# json file====json data====dictionary data

with open("new/demo.json",'r') as file:
    dic_data = json.load(file)
    print(dic_data)
    print(dic_data['Name'])
