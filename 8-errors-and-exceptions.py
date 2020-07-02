# how many kinds of errors?
print(2)

# handle exceptions
while True:
    try:
        x = int(input('Please enter a number: '))
        print('the square of {} is {}'.format(x, x ** 2))
        break
    except ValueError:
        print('Oops !')


def this_fails():
    return 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print(err)

# re-raise an exception
try:
    raise NameError('Hi there')
except NameError:
    print('An exception flew by !')
    raise
