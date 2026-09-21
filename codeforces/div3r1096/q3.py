import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    sixi = []
    twe = []
    tri = []
    oth = []

    for val in a:
        if val % 6 == 0:
            sixi.append(val)
        elif val % 3 == 0:
            tri.append(val)
        elif val % 2 == 0:
            twe.append(val)
        else:
            oth.append(val)

    soln = sixi + twe + oth + tri
    print(*soln)
    


t = int(input())
for _ in range(t):
    solve()