# List comprehensions
# These are a unique way of quickly creating a list with Python
# Ex: Using a for loop along with .append() to create a list,
# you can use the list comprehensions are a good alternative

# Without using the List compression
myString = "Hello"
mylist = []
for letter in myString:
    mylist.append(letter)

print(mylist)

print("###############")
# Using the List compression
myName = "Sathyavelrajan"
mylist = [x for x in myName]
print(mylist)
print("###############")

myNum = [x for x in range(10)]
print(myNum)

myNum = [x * x for x in range(10)]
print(myNum)

myNum = [x ** 2 for x in range(10) if x % 3 ==0]
print(myNum)

celcius = [0, 10, 20, 30, 39]
fahrehheit = [((9/5)* temp + 32) for temp in celcius]
print(fahrehheit)

results = [x if x%2 ==0 else "Odd" for x in range(1,11)]
print(results)

mylist = []
for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x*y)
print(mylist)

myNewlist = [x*y for x in [1, 3, 5] for y in [1, 10, 1000]]
print(myNewlist)