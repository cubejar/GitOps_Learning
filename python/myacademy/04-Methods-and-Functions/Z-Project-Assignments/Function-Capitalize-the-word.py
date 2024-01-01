'''
####
OLD MACDONALD:
Write a function that capitalizes
the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
Note: `'macdonald'.capitalize()`
returns `'Macdonald'`
'''

# def capitalize_macDonald(name):
#     newstr = []
#     for index, str in enumerate(name):
#         if index in [0, 3]:
#             newstr.append(str.upper())
#         else:
#             newstr.append(str.lower())
#     return "".join(newstr)
#
# print(capitalize_macDonald("macdonald"))

def capitalize_macDonald(name):
    str = ''
    for index,letter in enumerate(name):
        if index == 0 or index == 3:
            str = str + letter.upper()
        else:
            str = str + letter
    return str

print(capitalize_macDonald("macdonald"))