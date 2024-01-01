'''
Define a function called myfunc that takes in a string,
and returns a matching string where every even letter is uppercase,
and every odd letter is lowercase.
Assume that the incoming string only contains letters,
and don't worry about numbers, spaces or punctuation.
The output string can start with either an uppercase or
lowercase letter, so long as letters alternate throughout the string.

To give an idea what the function would look like when tested:
myfunc('Anthropomorphism')
# Output: 'aNtHrOpOmOrPhIsM'
Added note: this exercise requires that the function return a string.
'''
import stringprep


def myfunc(mystr):
    output_str = ""
    for idx,letter in enumerate(mystr):
        if (idx % 2) == 0:
            output_str += letter.upper()
        else:
            output_str += letter.lower()
    return output_str

print(myfunc("Anthropomorphism"))