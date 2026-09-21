import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = input().strip()

    zero = 0
    one = 0

    prezero = [0] * n
    preone = [0] * n

    prezero[0] = 0 if a[0] == '1' else 1
    preone[0] = 1 - prezero[0]

    for i in range(1, n):
        if a[i] == '0':
            prezero[i] = prezero[i-1] + 1
            preone[i] = preone[i-1]
        else:
            prezero[i] = prezero[i-1]
            preone[i] = preone[i-1] + 1

    # print(prezero)
    # print(preone)


    for val in a:
        if val == '0':
            zero += 1
        else:
            one += 1

    if a[0] == '1':
        return zero

    cost = float('inf')
    cnt = 0

    for i in range(n+1):
        curzero = 0 if i == 0 else preone[i-1]

        curone = prezero[-1] if i == 0 else prezero[-1] - prezero[i-1]

        cost = min(cost, curzero + curone)

    return cost

    











    # for val in a:
    #     if val == '0':
    #         zero_before = True
    #         if one_before:
    #             cnt += 1
    #             one -= 1
    #         else:
    #             zero -= 1

            
    #     if val == '1':
    #         if one_before:
    #             one -= 1
    #             continue

    #         if zero > one:
    #             if not zero_before:
    #                 one_before = True
    #                 one -= 1
    #             else:
    #                 cnt += 1
    #                 zero -= 1
    #         else:
    #             one_before = True
    #             one -= 1

    # return cnt


    


t = int(input())
for _ in range(t):
    print(solve()) 