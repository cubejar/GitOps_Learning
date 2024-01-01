# String => String immutability
# Are strings mutable?
# Strings are not mutable!
# IT means you can't use indexing to change individual elements of a string
name = "Sam"
# name[0] = "P" => Error out
newname = "P" + name[1:]
print(newname)
x = "Hello World."
y = " It is beautiful!"
print(x + y)
z = x[:5]
print(z*10)
print('3' + '7')
print(3 + 7)

print(x.upper())
print(x)
print(x.lower())
print(x)
print(x.split())

y = "This is a String"
print(y.split())
print(y.split('i'))