import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split())) 

    # naive approach
    """
    if you take sum of the subarray divide by the length

    """

    # presum = [0] * n
    # presum[0] = a[0]

    # for i in range(1, n):
    #     presum[i] = presum[i-1] + a[i]

    # print(presum)

    # can move from lower stack to higher stack
    # all stacks can be rearranged


    for i in range(n):
        a[i] = a[i] - i

    # print(a)

    a = sorted(list(set(a)))

    consec = 1
    max_consec = 1
    # print(a)

    for i in range(1, len(a)):
        if a[i] == a[i-1] + 1:
            consec += 1
        else:
            max_consec = max(max_consec, consec)
            consec = 1

    return max(max_consec, consec)




    


t = int(input())
for _ in range(t):
    print(solve()) 