myList = [1, 2, 3, 4, 5]
for jelly in myList:
    print(jelly)
print("##########")
for num in myList:
    if num % 2 ==0:
        print(num)
    else:
        print(f"Odd number : {num}")
print("##########")

sum = 0
for num in myList:
    sum = sum + num
print(sum)

print("##########")
mystring = "Hello World"

for letter in mystring:
    print(letter)

print("##########")

# Just in case if you don't intend to use the variable
for _ in "Good":
    print("Great")

print("##########")

# ITerate using Tuple

tup = (1, 2, 3, 3)

for item in tup:
    print(item)

print("##########")

mylist = [(1,2), (2,3), (3,4), (4,5)]
print(len(mylist))

print("##########")

# Iterating a sequnce of items that contains tuples,
# items can be used tuple unpacking
mylist = [(1,2), (2,3), (3,4), (4,5), (5,6)]
for item in mylist:
    print(item)

print("##########")
# tuple unpacking
mylist = [(1,2), (3,4), (5,6), (7, 8)]
for (a,b) in mylist:
    print(b)
print("##########")
# tuple unpacking
mylist = [(1,2), (3,4), (5,6), (7, 8)]
for a,b in mylist:
    print(a)

print("##########")
# tuple unpacking
mylist = [(1,2,3), (4,5,6), (7, 8,9)]
for a,b,c in mylist:
    print(b)
print("##########")
# Dictionary unpacking
mydict = {'k1':1, 'k2': 2, 'k3': 3}
for item in mydict.items():
    print(item)
print("##########")

mydict = {'k1':1, 'k2': 2, 'k3': 3}

for key in mydict.keys():
    print(key)

print("##########")

mydict = {'k1':1, 'k2': 2, 'k3': 3}

for value in mydict.values():
    print(value)
print("##########")

# Note: The dictionaries are unordered collection.
# So we can't expect the same order or sorted
mydict = {'k1':1, 'k2': 2, 'k3': 3}

for key,value in mydict.items():
    print(value)
print("##########")