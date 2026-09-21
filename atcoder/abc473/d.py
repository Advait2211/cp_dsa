import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())

    a = []
    for i in range(1, n + 1):
        a.append(k // i + 1)

    curr = [0] * n

    def generate(idx, total):
        if total > k:
            return

        if idx == n:
            if total == k:
                print(*curr)
            return

        for x in range(a[idx]):
            curr[idx] = x
            generate(idx + 1, total + x * (idx + 1))

    generate(0, 0)

    


t = 1
for _ in range(t):
    solve()