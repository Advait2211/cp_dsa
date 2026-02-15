def solve():
    n, x = map(int, input().split())

    la = -1 * float('inf')
    gain = [-1 * float('inf'), 0, 0, 0]

    for i in range(n):
        a, b, c = map(int, input().split())
        temp = a * b - c
        x -= a * (b-1) - c
        if temp > gain[0]:
            gain[0] = temp
            gain[1] = a
            gain[2] = b
            gain[3] = c
        elif temp == gain[0]:
            if b > gain[2]:
                gain[0] = temp
                gain[1] = a
                gain[2] = b
                gain[3] = c

        la = max(la, a * (b-1))

    if x <= 0:
        return 0
    
    

    if gain[0] <= 0:
        return -1
    
    # x -= la

    # jumps to reach new x
    import math
    # x += gain[1] * (gain[2]-1) - gain[3]
    print(x, gain)
    return math.ceil(x / gain[0]) + 1       
        

    """

    computing the rollbacks needed to reach the new x

    10 4
    0 - 4 1
    4 - 8 2
    8 - 10 3rd rollback only if we cannot cover that in less than b jumps


    """
    



t = int(input())
for _ in range(t):
    print(solve())
    print()