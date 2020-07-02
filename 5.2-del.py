words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# remove the first element
del words[0]
print(words)

# remove the slices from a list
del words[1:5:1]
print(words)

# clear the entire list
del words[:]

# del entire variables
del words
