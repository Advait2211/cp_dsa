import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    """
    monotonic hona chahiye na bas?
    edge cases of first and last elements

    find the first down
    then the up after however many down is allowed
    if there comes an down after the up, then we fail

    uff mb i understood the wrong question

    """


    # need = 0
    # base = a[0]
    # new_need = 0
    # basic = []

    # for i in range(n):
    #     # print(a[i])
    #     if a[i] >= base:
    #         base = a[i]
    #         basic.append(base)
    #     else:
    #         base = max(base, a[i]+need)
    #         basic.append(base)

    #         if need == 0:
    #             need = base - a[i]
    #         else:
    #             new_need = base - a[i]
    #             # print(f"{new_need=}")
    #             if new_need > need:
    #                 return "NO"
                
        
    #     # print(f"{base=}")
    #     # print(f"{need=}")
    #     # print(f"{new_need=}")



        

    # return "YES"

    mini = a[-1]
    reduction = 0

    for i in range(n-1, -1, -1):
        if a[i] <= mini:
            mini = a[i]
        else:
            mini = min(mini, a[i] - reduction)
            if reduction == 0:
                reduction = a[i] - mini
            else:
                if a[i] - reduction > mini:
                    return "NO"
                
        # print(f"{a[i]=}")
        # print(reduction)
        # print(mini)
                
    return "YES"








    


t = int(input())
for _ in range(t):
    print(solve()) 