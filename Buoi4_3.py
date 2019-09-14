def fibonacci_gen():
    a = 1
    while True:
        yield a
        a = a + 2
def fibonacci(n):
    i = -1
    for fib in fibonacci_gen():
        i+= 1
        if i == n:
            return fib
for n in range(10):
    print(fibonacci(n), end=" ")