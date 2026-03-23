import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    from collections import Counter
    # a = set(a)
    freq = Counter(a)
    a = sorted(a, reverse=True)

    print(freq)
    print(a)

    """
    1 3 1

    1 1 3 - 1 3 3
    1 3 1 - impossible
    3 1 1 - 3 3 1

    7 5 3 5 3 3 
    12 7 5 3
    """
    


t = int(input())
for _ in range(t):
    print(solve()) 