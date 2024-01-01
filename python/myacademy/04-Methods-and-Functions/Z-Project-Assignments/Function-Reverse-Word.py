'''
MASTER YODA: Given a sentence, return a sentence with the words reversed
    master_yoda('I am home') --> 'home am I'
    master_yoda('We are ready') --> 'ready are We'

Note: The .join() method may be useful here.
The .join() method allows you to join together strings
in a list with some connector string.
For example, some uses of the .join() method:
   // >>> "--".join(['a','b','c'])
   // >>> 'a--b--c'

This means if you had a list of words you wanted
to turn back into a sentence, you could just join
them with a single space string:
   // >>> " ".join(['Hello','world'])
   //  >>> "Hello world"
'''

# def master_yoda(str):
#     mylist = str.split(" ")
#
#     list_ind = []
#     for index, myst in enumerate(mylist):
#         list_ind.append(index)
#
#     rev_list_ind = list_ind[::-1]
#
#     newstrlist = []
#     for st in rev_list_ind:
#         newstrlist.append(mylist[st])
#
#     print(" ".join(newstrlist))

def master_yoda(text):
    myList = ''
    str = ''
    myList = text.split()
    # print(myList)
    myList.reverse()
    print(" ".join(myList))

master_yoda('I am home')
# master_yoda('We are ready')