def solve():
    n = int(input())
    a = list(map(int, input().split()))

    aso = sorted(a, reverse=True)

    i = 0

    while i < n and a[i] == aso[i]:
        i += 1

    if i == n:
        print(*a)
        return
    
    l = i

    r = a.index(aso[i])

    # print(a[l], a[r])

    a2 = a[l:r+1]
    # print(a2)

    a2 = a2[::-1]

    print(*(a[:l] + a2 + a[r+1:]))

    # print(a[i])
    # print(aso[i])



t = int(input())
for _ in range(t):
    solve()
    # print()