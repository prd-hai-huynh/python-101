words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

print(words.count('the'))
print(words.index('the'))
print(words.index('the', 3))
words.sort()
print(words)
words.reverse()
print(words)
print([w for w in words.copy()])

squares = [x ** 2 for x in range(10)]
print(squares)

vec = [-4, -2, 0, 2, 4]
# new list from vec
print([x * 2 for x in vec])
# filter
print([x for x in vec if x >= 0])
# apply function to all elements
print([abs(x) for x in vec])

# flatten a matrix using list-comp with 2 for
vec = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print([num for elem in vec for num in elem])

# nested list-comp
# example to transpose a matrix
print([[row[i] for row in vec] for i in range(3)])
