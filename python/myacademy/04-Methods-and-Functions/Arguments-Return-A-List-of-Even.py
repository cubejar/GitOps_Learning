'''
Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.
Remember, don't run the function, simply provide the definition.
To give an idea what the function would look like when tested:
myfunc(5,6,7,8)
# Output: [6, 8]
'''


def myfunc(*args):
    myList = []
    for num in args:
        if num % 2 == 0:
            myList.append(num)

    return myList

print(myfunc(5, 6, 7, 8))
