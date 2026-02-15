def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    bpsum = [0] * (n+1)

    for i in range(n):
        bpsum[i+1] = b[i] + bpsum[i]

    # print(bpsum)
    a = sorted(a)

    prev = -1

    freq = {}
    # strength, avail

    for i in range(n):
        if a[i] != prev:
            freq[a[i]] = n-i
            prev = a[i]

    # print(freq)

    # maxi = 0

    # for x, qty in freq.items():
    #     for i in range(1, n+1):
    #         reqd = bpsum[i]
    #         if qty >= reqd:
    #             maxi = max(maxi, x * i)
    #         else:
    #             continue

    # return maxi

    maxi = 0
    i = n

    for x in freq:
        qty = freq[x]
        while i > 0 and bpsum[i] > qty:
            i -= 1
        maxi = max(maxi, x * i)

    return maxi


    



t = int(input())
for _ in range(t):
    print(solve())