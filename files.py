"""
#create file
with open("example.text","w") as file:
    print("Created")

#Write file
with open("example.text","w") as file:
    file.write("Hello Python")

#Read file
with open("example.text","r") as file:
    content = file.read()
    print(content)


#Renaming          for renaming import os

import os
os.rename("example.text","new_example.text")


#Deleting
import os
os.remove("new_example.text")
"""


