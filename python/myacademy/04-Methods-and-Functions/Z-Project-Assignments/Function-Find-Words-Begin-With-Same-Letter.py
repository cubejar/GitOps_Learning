'''
####
ANIMAL CRACKERS: Write a function takes a two-word string
and returns True if both words begin with same letter
    animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False
'''

def animal_crackers(str):
    myList = str.split()
    if myList[0][0].lower() == myList[1][0].lower():
        print(True)
    else:
        print(False)

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')
