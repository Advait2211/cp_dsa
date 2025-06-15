import math

def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    soln = 0

    ans = [i for i in range(n + 1) if primes[i]]

    for i in ans:
        soln += math.floor(n / i)

    # soln = math.floor(n / 2)
    return soln

def solve():
    n = int(input())
    return sieve_of_eratosthenes(n)


t = int(input())

for _ in range(t):
    print(solve())
