# https://codeforces.com/problemset/problem/1981/B

"""

"""

def solve():
    n, m = map(int, input().split())

    l = max(0, n - m)
    r = n + m
    res = 0

    for i in range(l, min(r + 1, l + 64)):
        res |= i
    return res

t = int(input())

for _ in range(t):
    print(solve())
