def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
n = 10
print(list(fibo(n)))
