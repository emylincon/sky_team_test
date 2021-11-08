fib = lambda x: fib(x-2) + fib(x-1) if x >=2 else x

print(fib(10))

