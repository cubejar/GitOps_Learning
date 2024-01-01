# Dictionaries are """"unordered"""" mappings for storing objects
# Dictionaries use key-value pairing
# This key value pair allows users to """"quickly""" grab objects
# So we don't need to know an index location
# Dictionaries uses curly braces, and colons
# Dictionaries are """""not""""" able to sort

# Dictionaries are abjects retrieved by a key name
# They are unordered and can't be sorted
# Lists are objects retrieved by location
# They are ordered sequence
# They can be indexed or sliced

mydict = {'name': "Rajan", 'age': 46, 'Color': "Blue", "Favorite_Fruit": "Apples"}
print(mydict)
print(mydict["name"])
print(mydict["Favorite_Fruit"])

mixed_dict = {'k1': 123,
              'k2': [1, 2, 4],
              'k3': {'key1': 30,
                     'inside_key': 100,
                     'key4': "Nice",
                     'key3': 34.3
                     }
              }
print(mixed_dict['k3']['key4'].upper())
print(mixed_dict['k3'].values())

## Assign new values to the dict
mixed_dict['k2'] = "This has changed"
print(mixed_dict)

## Obtain all the keys
print(mixed_dict.keys())

## Obtain all the keys
print(mixed_dict.values())

## Obtain both keys and values ==> This will be a Tuple
print(mixed_dict.items())
