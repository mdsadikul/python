#lambda function: Python-এ lambda function হলো ছোট, একলাইনের anonymous function (নাম ছাড়া ফাংশন)।
#Basic syntax:      lambda arguments : expression


result= lambda: 2+5
print(result())

add= lambda x,y: x+y
print(add(10,50))

result= lambda x,y: x if x>y else y
print(result(10,50))