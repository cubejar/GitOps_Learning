'''FIND 33:
Given a list of ints, return True if the array
contains a 3 next to a 3 somewhere.
    has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False
'''

def has_33(my_list):
    x = 0
    list_len = len(my_list)
    mybool = True
    for x in range(list_len - 1):
        if my_list[x] == my_list[x + 1] == 3:
            mybool = True
            break
        else:
            x += 1
            mybool = False
            continue
    print(mybool)


has_33([1, 2, 3, 1])
has_33([1, 5, 2, 3])
has_33([1, 3, 3])
has_33([1, 4, 6, 3, 1, 3, 5, 3, 3, 4, 5, 3])