def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # l = []
    # r = []

    prefix = [-1] * n
    prefix[-1] = max(a[-1], b[-1])


    for i in range(n-2, -1, -1):
        prefix[i] = max(prefix[i+1], a[i], b[i])

    psum = [0] * (n + 1)

    for i in range(n):
        psum[i + 1] = psum[i] + prefix[i]

    # print(prefix)
    # print(psum)
    
    soln = []

    for _ in range(q):
        l, r = map(int, input().split())
        soln.append(psum[r] - psum[l - 1])

    print(*soln)



t = int(input())
for _ in range(t):
    solve()