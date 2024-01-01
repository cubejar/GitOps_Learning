# Use for, .split(), and if to create a statement that will print out
# the words that starts with "s"
# mystr = "Print only the words that start with s in this sentence

mystr = "Print only the words that start with s in this sentence"
myList = mystr.split()
myNewList = []
print(myList)
for word in myList:
    if(word[0] == "s"):  # word[0].lower() == "s"
        myNewList.append(word)
    else:
        continue
print(" ".join(myNewList))
