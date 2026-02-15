import sys
input = sys.stdin.readline

def solve():
    n, m, h = map(int, input().split())
    a = list(map(int, input().split()))

    add = [0] * n
    last = [0] * n

    ct = 0
    reset = 0

    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        ct += 1

        if last[x] < reset:
            add[x] = 0

        val = a[x] + add[x] + y

        if val > h:
            reset = ct
        else:
            add[x] += y
            last[x] = ct

    for i in range(n):
        if last[i] >= reset:
            a[i] += add[i]

    print(*a)


t = int(input())
for _ in range(t):
    solve()
