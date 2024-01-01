# Lists are orderned sequences
# Can hold mixed variety of objects
# They are mutable
# They use [] and separate objects
# They can hold duplicates
# They can support indexing and slicing
# Lists can be nested

my_1_list = [1, 2, 3, 3, 44, 55, 22]
my_2_list = [4, 5, 6, 7]
my_2_list = my_1_list + my_2_list
print(my_2_list[3:])

## Append
my_2_list.append(8)
print(my_2_list)
my_2_list.append(10)
print(my_2_list)

## Pop an item at the end
my_2_list.pop()
print(my_2_list)

# Remove an item
my_2_list.remove(2)
print(my_2_list)

# Get the item based on the index
print(my_1_list[-1])

# Pop an item based on index
print(my_1_list)
print(my_1_list.pop(1))
print(my_1_list)

# In place sort.
# It will not return anything to assign
alph_list = ['a', 'e', 'x', 'd', 'r', 'b']
alph_list.sort()
print(alph_list)
abc = alph_list.sort()
print(type(abc))

# Sorted method to use to sort the items - It's not an "in place" sort
beta_list = ['a', 'e', 'x', 'w', 'd', 'r', 'b']
new_list = sorted(beta_list)
print(new_list)
print(type(new_list))

# Reverse method - "In place" - It will not return
alph = ['a', 'z', 'x', 'w', 'b']
print(alph.reverse())
print(alph)

