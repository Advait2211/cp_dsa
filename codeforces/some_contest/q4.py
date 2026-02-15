def solve():
    n, m, k = map(int, input().split())

    left = k - 1
    right = n - k
    # l, r = 0, 0
    # ans = 0


    # while m > 0:
    #     val = (1 << l)
    #     val2 = (1 << r)

    #     if l < left:
    #         if m >= val:
    #             ans += 1
    #             m -= val
    #             l += 1
    #     if r < right:
    #         if m >= val2:
    #             ans += 1
    #             m -= val2
    #             r += 1

    #     if val > m and val2 > m or l>=left and r>=right:
    #         break


    # print(ans)

    l = r = 0
    ans = 0

    while m > 0 and (l < left or r < right):
        did = False

        if l < left:
            val = 1 << l
            if m >= val:
                m -= val
                ans += 1
                l += 1
                did = True

        if r < right:
            val2 = 1 << r
            if m >= val2:
                m -= val2
                ans += 1
                r += 1
                did = True

        if not did:
            break

    return (ans+1)



t = int(input())
for _ in range(t):
    print(solve())