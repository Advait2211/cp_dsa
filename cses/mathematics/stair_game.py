def solve():
    n = int(input())
    a = list(map(int, input().split()))

    xor = 0
    mex = 0

    for i in range(n):
        if i % 2 == 0:
            pass
        xor ^= (a[i] % 2)

    # print(xor)
    if xor == 0:
        return("second")
    else:
        return("first")



t = int(input())
for _ in range(t):
    print(solve())