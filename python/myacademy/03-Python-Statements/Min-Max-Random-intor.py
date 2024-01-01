myList = [1, 2, 3, 4, 5, 6]
# min
print(min(myList))
# max
print(max(myList))
# random
# Import a function from a library
from random import shuffle


print("############")
myList = [1, 2, 3, 4, 5, 6, 7]
shuffle(myList)
print(myList)
print("############")
# from random import randomX
from random import randint
print(randint(0, 50))