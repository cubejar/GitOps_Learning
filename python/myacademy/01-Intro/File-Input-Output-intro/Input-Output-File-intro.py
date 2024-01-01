# open('zyz.tzt')
# read()
# readline()

myfile = open('test.txt')

print(myfile.read())
print("This is the end!!!")

myfile.seek(0)
print(myfile.read())
print("!!End of Second !!!")

myfile.seek(0)
print(myfile.readlines())
print("!!Final !!!")


