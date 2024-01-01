# Zip two lists together => Returns a tuple
myNumList = [1, 2, 3]
myAlphaList = ['a', 'b', 'c']
for item in zip(myAlphaList, myNumList):
    print(item)
print("###############")

# Zip 3 lists together
myNumList = [1, 2, 3]
myAlphaList = ['a', 'b', 'c']
myColor = ['Red', 'Blue', 'White']
for item in zip(myAlphaList, myNumList, myColor):
    print(item)
print("###############")

# Zip 3 lists together - uneven.
# It will omit the values that are not matching
# It won't throw any error
myclass = ['1st', '2nd', '3rd']
myNum  = [1, 2, 3]
myPosition = ["First", "Second", "Third"]
for item in zip(myclass, myNum, myPosition):
    print(item)
print("###############")

# Zip and get it as a list
myPlanets = ['earth', 'venus', 'saturn']
myNum  = [1, 2, 3]
myPosition = ["Third", "Four", "Seven"]
print(list(zip(myPlanets, myNum, myPosition)))
print("###############")

# Tuple unpacking
festivals = ["Diwali", "Pongal", "Chadhurthi", "Onum"]
special = ['Snacks', 'Sugar cane', 'Apple', "Flowers"]
myPosition = ["Third", "Four", "Seven"]
for key, _, val in zip(festivals, special,myPosition):
    print(_)

print("###############")
# In key word
if 'a' in "Sathyavelrajan":
    print(True)
else:
    print(False)
print("###############")
# In key word - List
myList = [1, 3, 5, 7]
if 5 in myList:
    print(True)
else:
    print(False)
print("###############")
# In key word - Dictionary
myDict = {"k1": 100, "k2": 200, "k3": 400}
if 200 in myDict.values():
    print(True)
else:
    print(False)

print("###############")
# In key word - Dictionary
myDict = {"k1": 100, "k2": 200, "k3": 400}
if 200 in myDict.keys():
    print(True)
else:
    print(False)
print("###############")
