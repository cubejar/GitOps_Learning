# Range function for iterations
for num in range(10):
    print(num)

for gen in range(5,10):
    print(gen)

for gen in range(100,106, 2):
    print(gen)

# Generators => Special type of function to generate information
# It will not save it in the memory
# Efficient way of using the function - Ex: range

vals = range(0,10,2)
print(vals)

myList = list(range(0,10,2))
print(myList)

print(list(range(0,10,2)))
