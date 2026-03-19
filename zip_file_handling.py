"""
#creating zip file

import zipfile
with zipfile.ZipFile("new.zip","w") as zip:
    zip.write("demo1.text")
    zip.write("demo2.text")

#Extract from Zip file

import zipfile
with zipfile.ZipFile("new.zip","r") as zip:
    zip.extractall()
    extracted_files = zip.namelist()
    print(extracted_files)

"""
#Make zip from directory

import shutil
shutil.make_archive("new_new",'zip','new')
