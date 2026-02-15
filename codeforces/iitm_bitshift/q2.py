def solve():
    n, m = map(int, input().split())
    s = input()

    a = list(map(int, input().split()))

    # s = "10101"
    # s += '0' * 2
    # print(s)

    # print(s[:2])

    sm = 0
    mn_sm = 0

    for val in a:
        sm += val
        mn_sm = min(mn_sm, sm)

    val = len(s) - abs(mn_sm)

    if val <= 0:
        return "0"
    else:
        # return s[:-sm] + "0" * sm
        s = s[:val] + '0' * abs(mn_sm)
        if sm < 0:
            # right shift
            sm = abs(sm)
            s = s[:-sm]
        else:
            # left shift
            s += '0' * sm

        return s

    # for k in a:
    #     if k < 0:
    #         # right shift
    #         k = abs(k)

    #         if k >= len(s):
    #             return '0'
    #         else:
    #             s = s[:-k]
    #     else:

    #         # left shift
    #         s += '0' * k

    #     # print(s)

    # # print(s)
    # return(s)

    



t = int(input())
for _ in range(t):
    print(solve())