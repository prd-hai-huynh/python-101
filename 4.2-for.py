# basic
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# loop over a copy
tuples = [(1, 2), (3, 4)]
for x, y in tuples.copy():
    print('x={x}, y={y}'.format(x=x, y=y))
