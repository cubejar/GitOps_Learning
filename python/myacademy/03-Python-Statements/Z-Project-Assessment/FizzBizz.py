for x in range(1,101,1):
    if (x%5) == 0 and (x%3 ==0):
        print("FizzBuzz", x)
    elif x%5 == 0:
        print("Buzz", x)
    elif x%3 == 0:
        print("Fizz", x)
    else:
        print(x)
