# Sets are unordered collection of """"unique"""" elements
# There can only be one representative of the same object.
# It looks like dictionary. However, it's not a key-value pairs
# It's just an unordered collection of any items that you want
# It can be retuned in any order

mysets = set()
print(mysets)

### Add method
mysets.add(1)
print(mysets)
mysets.add(1)
print(mysets)

myList = [1, 2, 3, 1, 2, 1, 1, 2, 3, 4, 2, 1, 2, 2, 1, 4, 0, 5, 2, 3]
myset = set(myList)
print(myset)

# It can be retuned in any order
myalpset = set('Mississippi is nice')
print(myalpset)
# {'M', 'i', 's', 'p', 'e', 'n', 'c', ' '} or {'s', 'i', 'n', ' ', 'e', 'M', 'c', 'p'}

# {1,2,3,4} is an example of a Set.
# True

# How do you add an element to a set?
# .add() method

# What is the result of:
# set([1,1,2,3])
# {1, 2, 3}