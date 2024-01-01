myStr = "Create a list of the first letters of every word in this string"
mySplitStr = []
mySplitStr = myStr.split()
print(mySplitStr)
myList = [x[0] for x in mySplitStr]
print("".join(myList))