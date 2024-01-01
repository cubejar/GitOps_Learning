myStr = "Print every word in this sentence that has an even number of letters"
myStrList = myStr.split()
mynewstr = []
for word in myStrList:
    if len(word)%2 ==0:
        mynewstr.append(word)
    else:
         continue
print(mynewstr)
print(" ".join(mynewstr))

# for word in myStr.split():
#     if len(word) % 2 == 0:
#         print(word)