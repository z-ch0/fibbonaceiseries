def fibon(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
n = 10
print(list(fibon(n)))
