def fib(n=1):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


print(fib)
print(type(fib(0)))
fib()
fib(2000)
