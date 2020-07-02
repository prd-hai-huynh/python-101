dict1 = {'k1': 1, 'k2': 2, 'k3': 3}
print(dict1)
del dict1['k1']
print(dict1)
dict1['k0'] = 0
print(dict1)
print(list(dict1))
print(sorted(dict1))
print('k1' in dict1)
print('k5' not in dict1)

dict2 = dict([('k1', 1), ('k2', 2), ('k3', 3)])
print(dict2)

# dict comprehensions
d = {x: x ** 2 for x in range(5)}
print(d)
