import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    v = list(map(int, input().split()))

    a = []
    pre = [0]

    for i in range(n):
        m = sorted(list(map(int, input().split())), reverse=True)
        # pre.append(pre[-1] + sum(m))
        a.append(m)

    print(a)
    print(pre)
    
    


t = int(input())
for _ in range(t):
    print(solve()) 