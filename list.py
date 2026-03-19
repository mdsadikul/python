fruits = ['app', 'bana','water',12,13,14,15,2.33,3.33]
print(fruits)
fruits.append('hola')
print(fruits)
fruits.pop()
print(fruits)
print(id(fruits))
print(id(fruits[2]))
list_mix = fruits.copy()
print(list_mix)

fruits.insert(0,"sadik")
print(fruits)

fruits2 = ['hola','lolo','yolo','les']
fruits.extend(fruits2)
print(fruits)

fruits.remove(15)
print(fruits)

for item in fruits:
    print(item)

list_mix.clear()
print(list_mix)

print(len(fruits))
print(len(list_mix))
print(fruits.count('app'))

li = [2,3,4,1,5]
li.sort()
print(li)