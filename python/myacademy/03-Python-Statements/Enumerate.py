# Not using the Enumerator
# To print the index count and the value
index = 0
for num in 'abcde':
    print('At index {}, we have the letter: {}'.format(index, num))
    index += 1

# Not using the Enumerator
# To print the index count and the value
index = 0
word = "Sathyavelrajan"
for letter in word:
    print(word[index])
    index += 1

# Using the Enumerator, to print the index count and the value
# It returns a tuple
word = "Sathyavelrajan"
for item in enumerate(word):
    print(item)

# Using the Enumerator, to print the index count and the value
word = "Sathyavelrajan"
for idx, letter in enumerate(word):
    print(idx)
    print(letter)
    print("\n")