import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    from collections import Counter
    freq = Counter(a)

    sm = 0

    for key, value in freq.items():
        sm += (value % 2) * key

    return sm
    


t = 1
for _ in range(t):
    print(solve()) 