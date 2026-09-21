import sys
input = sys.stdin.readline

def prime_factors(n):
    if n < 2:
        return []

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2

    if n > 1:
        factors.append(n)

    return factors



def recur(n, k, dp):
    if n <= k:
        return 0

    if dp[n] != -1:
        return dp[n]

    factors = prime_factors(n)

    best = float('inf')

    for i in range(len(factors)):
        best = min(best, 1 + factors[i] * recur(n//factors[i], k, dp))

    dp[n] = best
    return best

    


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = 0

    dp = [-1] * (max(a) + 1)

    for i in range(n):
        if a[i] <= k:
            continue

        cnt += recur(a[i], k, dp)
        # print(a[i], end = " ")
        # print(cnt)

    # print(dp)


        

    return cnt


    


t = int(input())
for _ in range(t):
    print(solve()) 