def solve():
    n, k = map(int, input().split())
    a = input()
    op = [1] * n

    if n == k:
        for i in range(n):
            op[i] = '-'
        print(''.join(op))
        return

    upper_c = 0
    lower_c = 0
    random_action = 0

    for c in a:
        if c == '0':
            upper_c += 1
        elif c == '1':
            lower_c += 1
        else:
            random_action += 1

    # print(upper_c, lower_c, random_action)

    

    
    """

    declare an array on size n
    append all the minuses in the beginning

    now all that remains are the plusses and the question marks
    at max, we can have 
    + = n - (top + bottom + 2 * ra)


    so we only check if question mark comes or not
    if it does not come, we can just append all the question marks
    """

    for i in range(upper_c):
        op[i] = '-'

    for i in range(n - lower_c, n):
        op[i] = '-'

    total = upper_c + lower_c + 2 * random_action
    plusses = n - total

    if plusses > 0:
        mid_start = upper_c
        mid_end = n - lower_c

        mid_len = mid_end - mid_start
        plus_start = mid_start + (mid_len - plusses) // 2
        plus_end = plus_start + plusses

        for i in range(mid_start, mid_end):
            if plus_start <= i < plus_end:
                op[i] = '+'
            else:
                op[i] = '?'
    else:
        for i in range(upper_c, n - lower_c):
            op[i] = "?"
        # if total > n:
        #     # the common elements will again have minus
        #     common = total - n
        #     start = (n - common) // 2
        #     end = start + common

        #     for i in range(start, end):
        #         op[i] = '-'

        #     ##

        #     mid_start = upper_c
        #     mid_end = n - lower_c

        #     mid_len = mid_end - mid_start
        #     cm_start = mid_start + (mid_len - common) // 2
        #     cm_end = cm_start + common

        #     for i in range(mid_start, mid_end):
        #         if cm_start <= i < cm_end:
        #             op[i] = '-'
        #         else:
        #             op[i] = '?'

        # else:
        

    print(''.join(op))


    



t = int(input())
for _ in range(t):
    solve()