import sys
input = sys.stdin.readline

def get_factors(n):
    factors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors += 1
            if i*i != n:
                factors += 1
    return factors

def solve():
    x, y = map(int, input().split())

    import math

    diff = abs(x - y)

    print(max(1, get_factors(diff)))

    # print(get_factors(6))
    # n! / ()

    a = [0] * (x+y)

    for i in range(x):
        a[i] = 1
    for i in range(x, x+y):
        a[i] = -1

    print(*a)

    # versions = math.factorial(x+y) / (math.factorial(x) * math.factorial(y))

    # return versions * diff % 676767677

    


t = int(input())
for _ in range(t):
    solve()