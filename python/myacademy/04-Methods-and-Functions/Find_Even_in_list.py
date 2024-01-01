# Use snake casing: use lowercase letters and connect words using "_"
# """ used to mention docstring to explains functions: Comment """
# """ """" It is a multi-line string to describe function
# Normally we use the return inside the function
# We don't use Print inside the functions in general

myL = [1, 2, 3, 4, 5]

# Allows you to store the function result
def name_of_function(a, b):
    return a+b

# Won't allow you to store the function result
def print_function(a, b):
    print(a+b)

# Make sure to check the datatype of return
# Make sure to check the datatype on the function return
# Ex: name_of_function(10, 20)     ==> 30
# Ex: name_of_function('10', '20') ==> 1020

# Find even number in a list. Make sure to return at the end
def find_even_number_in_list(mylist):
    for num in mylist:
        if num % 2 ==0:
            return True
        else:
            pass   # return False ##### WRONG!!!!
    return False

print(find_even_number_in_list([1,5,3]))
print(find_even_number_in_list([2,4,3]))
print(find_even_number_in_list([1,3, 4, 9]))

