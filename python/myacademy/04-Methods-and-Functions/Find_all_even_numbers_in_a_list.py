def find_all_even_from_list(mylist):
    # Placeholder variables
    mynewlist = []

    for num in mylist:
        if num % 2 == 0:
            mynewlist.append(num)
        else:
            pass

    return mynewlist

print(find_all_even_from_list([1,3,4,2,8,3,10,11]))

print(find_all_even_from_list([11,5,7]))