dict1 = {'k1': 1, 'k2': 2, 'k3': 3}
for k, v in dict1.items():
    print('{0}: {1}'.format(k, v))

for i, v in enumerate(['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']):
    print('{0}: {1}'.format(i, v))

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]
for v1, v2 in zip(l1, l2):
    print('{0}: {1}'.format(v1, v2))
