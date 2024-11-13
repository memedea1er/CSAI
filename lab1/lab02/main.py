def eratosthenes_sieve(limit):
    primes = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if primes[p] == True:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1

    return [p for p in range(2, limit + 1) if primes[p]]

n = int(input("Введите предел для поиска простых чисел: "))

print(f"Простые числа до {n}: {eratosthenes_sieve(n)}")
