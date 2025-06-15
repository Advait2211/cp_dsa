import math

def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]

def solve():
    n = int(input())
    soln = 0

    ans = sieve_of_eratosthenes(n)

    for i in ans:
        soln += math.floor(n / i)

    print(ans)

    # soln = math.floor(n / 2)
    return soln
    
    
            



t = int(input())

for _ in range(t):
    print(solve())

# print(sieve_of_eratosthenes(10))