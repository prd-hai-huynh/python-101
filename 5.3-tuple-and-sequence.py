# tuple packing
t = 12345, 54321, 'string',
u = t, 1, 2, 3, 4, 5
print(u)

empty = ()
singleton = '12345',
print(len(empty))
print(len(singleton))
print(len(singleton[0]))

# sequence unpacking
x, y, z = t
print(x, y, z)
