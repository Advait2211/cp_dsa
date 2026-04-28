import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if len(set(a)) != len(a):
        print(-1)
        return
    
    if 0 in a:
        print(-1)
        return
    
    a = sorted(a, reverse=True)
    print(*a)

    


t = int(input())
for _ in range(t):
    solve()