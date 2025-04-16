def crivello(n):
    numeri = set(range(2, n + 1))
    for i in range(2, int(n**0.5) + 1):
        if i in numeri:
            numeri -= {i * x for x in range(2, n // i + 1)}
    return numeri

res = crivello(100)
print(len(res))
print(sorted(res))
