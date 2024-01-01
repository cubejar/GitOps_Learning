# Tuples are similar to Lists
# Tuples can't be changed
# They are Ordered sequence of objects
# They are immutable

# Once an element is inside a tuple, it can't be reassigned
# Tuple uses Parenthesis
# Ex: (1, 2, 3)

tup = (1, 2, 3, "Nice")
print(tup)
print(type(tup))
print(len(tup))

print(tup[3].upper())
print(tup[2])

### Count method
tupl = ('a', 'a', 'b', 'a', 'c', 'a', 'z', 'a', 'a')
print(tupl.count('a'))

### Index method - returns only the first index of that item
tupl = ('a', 'a', 'b', 'a', 'c', 'a', 'z', 'a', 'a')
print(tupl.index('b'))

tupl = (1000, 4004)
print(tupl)

# 'tuple' object does not support item assignment
# tupl[0] = 5000  => Not possible
# Data integrity

# Tuples have a lot of methods associated with them.
# False. There are only two methods for tuples!

# Tuples are Immutable.
# True

# Tuples can hold other objects.
# (1, 2, [1,2])
# Even though a list is one of the elements, the object constrained with () is a tuple!
