fib = lambda x: fib(x-2) + fib(x-1) if x >=2 else x

limit = input("How many fibonacci numbers would you like to print? ")
try:
    limit = int(limit)
except ValueError:
    print("Please enter an integer")

for i in range(limit):
    print(fib(i))
