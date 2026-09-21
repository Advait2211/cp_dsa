import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    opr = 0
    idx = []

    for i in range(n-1, -1, -1):
        if (a[i] > 0 and opr % 2 == 0) or (a[i] < 0 and opr % 2 == 1):
            idx.append(i+1)
            opr += 1

    print(len(idx))
    print(*idx)
        


    


t = int(input())
for _ in range(t):
    solve()