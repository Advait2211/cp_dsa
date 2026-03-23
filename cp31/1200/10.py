import sys
input = sys.stdin.readline

def solve():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    psum = [0] * (n+1)
    for i in range(n):
        psum[i+1] = psum[i] + a[i]

    pmax = [0] * (n+1)
    for i in range(n):
        pmax[i+1] = max(pmax[i], a[i])

    # print(psum)
    # print(pmax)

    import bisect
    for q in queries:
        idx = bisect.bisect_right(pmax, q)
        print(psum[idx-1], end = " ")


    


t = int(input())
for _ in range(t):
    solve()
    print()