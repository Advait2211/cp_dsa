import sys
input = sys.stdin.readline

def solve():
    # n = int(input())
    a = input().strip()

    n = len(a)

    for i in range(n):
        print(a[i], end = "")

        if i != n-1:
            print('o', end = "")

    


t = 1
for _ in range(t):
    solve()