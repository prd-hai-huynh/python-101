words = {'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'}

# the second word [the] will be disappeared
print(words)
print('the' in words)

# the second way to construct set
a = set('abcdef')
b = set('cdefgh')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# set comprehensions
x = {x for x in 'cdefgh' if x not in 'abc'}
print(x)
