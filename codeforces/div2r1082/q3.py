def solve():
    n = int(input())
    a = list(map(int, input().split()))

    mini = a[0]
    maxi = a[0]

    count = 1

    for i in range(1, n):
        cur = a[i]

        if cur > mini and cur <= max(maxi, a[i-1]+1):
            # maxi = max(maxi, cur)

            # if cur < maxi:
            #     maxi = cur
            maxi = cur
        else:
            # print(f"{i=}")
            count += 1
            mini = cur
            maxi = cur

    return count



t = int(input())
for _ in range(t):
    print(solve())