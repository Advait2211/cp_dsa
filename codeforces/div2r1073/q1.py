def solve():
    n = int(input())
    a = list(map(int, input().split()))

    m1 = {}
    m2 = {}

    for i in range(n):
        if i % 2 == 0:
            m1[a[i]] = 1
            m2[a[i]] = 0
        else:
            m1[a[i]] = 0
            m2[a[i]] = 1

    # print(m1, m2)

    a = sorted(a)

    f1, f2 = True, True

    for i in range(1, n):
        if m1[a[i]] == m1[a[i-1]]:
            f1 = False
            break

    for i in range(1, n):
        if m2[a[i]] == m2[a[i-1]]:
            f2 = False
            break
    

    if f1 or f2:
        return "YES"
    else:
        return "NO"



t = int(input())
for _ in range(t):
    print(solve())