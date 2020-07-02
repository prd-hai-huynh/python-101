# default argument values
def add(a=0, b=0):
    return a + b


print(add())


# L is mutable
def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(1))
print(f(2))


# keyword arguments
# ref: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
def kw(arg, *args, **kwargs):
    print('arg is a', type(arg))
    print('args is a', type(args))
    print('kwargs is a', type(kwargs))
    print(arg, args, kwargs)


kw(1, 2, x=1, y=2, z=3)


# keywords only function
def kwo(*, a, b):
    print(a, b)


kwo(a=1, b=2)


# duplicated arg names
def foo(name, **kwargs):
    print('name: ', name)
    return 'name' in kwargs


# todo: comment this line to run the next functions
print(foo(1, name=11))


def concat(*args, sep='.'):
    return sep.join(args)


print(concat("earth", "mars", "venus"))

# lambda function
pairs = [(1, 'd'), (2, 'c'), (3, 'b'), (4, 'a')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
