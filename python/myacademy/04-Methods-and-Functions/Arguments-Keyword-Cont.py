# Kwargs - Takes as many values, We could pick a specific arg
def myFunc(**kwargs):
    if 'fruit' in kwargs:
        print("My favorite fruit is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit here!")


myFunc(veggie='Lettuce', color="Green", fruit="Apple")
