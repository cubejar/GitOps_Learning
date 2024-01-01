# Positional Arguments
# It takes a tuple

def positional_arguments(arg1, arg2, points=10):
    return sum((arg1, arg2, points)) * 0.05


print(positional_arguments(40, 60))

print("#######################")


# To specify all the positional argumetns, you can specify it *args

def myfunc(*args):
    return sum(args) * 0.05


print(myfunc(40, 50, 60, 70))
print(myfunc(50, 40, 20, 10, 30, 70, 30, 20, 90))

print("#######################")



def myfunction(*args):
    for item in args:
        print(item)


print(myfunction(40, 60, 100, 1, 34))

print("########################")