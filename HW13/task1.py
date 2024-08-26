def fibonacci_generator(n):

    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = int(input("Enter value :"))

fib_gen = fibonacci_generator(n)
for num in fib_gen:
    print(num)
