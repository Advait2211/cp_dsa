import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = input()

    s = set()
    sm = 0

    for i in range(n):
        if a[i] not in s:
            s.add(a[i])
            sm += n - i

    return sm

    


t = int(input())
for _ in range(t):
    print(solve()) 