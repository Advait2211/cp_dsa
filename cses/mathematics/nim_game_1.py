def solve():
    n = int(input())
    a = list(map(int, input().split()))

    xor = 0

    for val in a:
        xor ^= val

    # print(xor)
    if xor == 0:
        return("second")
    else:
        return("first")



t = int(input())
for _ in range(t):
    print(solve())