# ------------------Creating a Directory------------------
"""
import os
os.mkdir("new")

#reading a directory
import os
dirItems = os.listdir(".")          #we can see all directory in a list using "."
print(dirItems)


#Writing to a file in a ditectory

import os
with open("new/test.text","w") as file:
    file.write("sadik f")

#Renaming a Directory
import os
os.rename("new","new_new")



#deleting a directory

import os
os.remove("new_new/test.text")          #first delete file in the directory
os.rmdir("new_new")
"""

#Read files name from directory and print as a list
import os
file_list = os.listdir("new")
#print(file_list)
for file_name in file_list:
    print(file_name)





