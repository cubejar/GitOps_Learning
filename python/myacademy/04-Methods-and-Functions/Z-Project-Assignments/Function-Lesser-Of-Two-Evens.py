'''Write a function that returns the lesser of two
given numbers if both numbers are even,
but returns the greater if one or both numbers are odd
    lesser_of_two_evens(2,4) --> 2
    lesser_of_two_evens(2,5) --> 5
'''
# def lesser_of_two_evens(arg1, arg2):
#     if arg1 % 2 == 0 and arg2 % 2 == 0:
#         if arg1 < arg2:
#             return arg1
#         else:
#             return arg2
#     else:
#         if arg1 < arg2:
#             return arg2
#         else:
#             return arg1
#
#
# print(lesser_of_two_evens(2, 4))
# print(lesser_of_two_evens(2, 7))

def lesser_of_two_evens(a,b):
    if a < b and (a % 2 == 0 and b % 2 == 0) :
        return a
    elif b > a and (a % 2 != 0 or b % 2 != 0):
        return b
    else:
        pass

print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 9))

