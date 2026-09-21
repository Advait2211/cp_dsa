import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = input().strip()

    from collections import Counter
    freq = Counter(a)

    odd = 0
    even = 0

    for key, value in freq.items():
        if value % 2 == 0:
            even += 1
        else:
            odd += 1

    if k >= (odd-1):
        return "YES"

    return "NO"


t = int(input())
for _ in range(t):
    print(solve()) 