import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    init = 2 * n

    for i in range(n):
        print(init, end = " ")
        init -= 1

    


t = int(input())
for _ in range(t):
    solve()
    print()