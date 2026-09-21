import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    from collections import Counter

    freq = Counter(a)

    mx = 0

    for key, value in freq.items():
        mx = max(mx, value)

    ans = 0

    for key, value in freq.items():
        ans += 1 if (value == mx) or (value == mx-1) else 0

    return ans


    


t = 1
for _ in range(t):
    print(solve()) 