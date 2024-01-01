# Keyword arguments
# It returns the dictinary
# Keyword Arg and Positional args will be used when using outside libraries

def myfunc(**kwargs):
    print(kwargs)

myfunc(fruit="Apple", veggie="Lettuce")