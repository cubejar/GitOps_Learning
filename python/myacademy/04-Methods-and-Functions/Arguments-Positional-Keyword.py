def myfunc(*args, **kwargs):
    # print(args)     # Tuple
    # print(kwargs)   # Dictionary
    print("I would like to find my {} {}".format(args[0], kwargs['animal']))


myfunc(10, 20, 30, 40, fruit='Orange', food='Pasta', animal="Dogs")
