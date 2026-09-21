import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    temp = n // 2

    sm = 0

    for i in range(n):
        if i >= temp:
            sm += a[i]

    return sm
    


t = 1
for _ in range(t):
    print(solve()) 