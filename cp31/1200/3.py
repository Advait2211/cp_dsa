import sys
input = sys.stdin.readline

def solve():
    n, x, y = map(int, input().split())

    """
    x divisible max val
    y divisible min val

    x - y divisible does not matter

    solve a question
    12 6 3 - n x y

    1 2 3 4 5 6 7 8 9 10 11 12

    6 12 - 1 2 = -3

    we don't have to return the permutation. 

    the answer would be
    if x == y: 0

    so basically the algorithm would be something like
    ignore the common and the non divisible values

    x
    y
    lcm

    x: n + n-1 + n-2 (x-lcm times)
    y: 1 + 2 + 3 + (y-lcm times)

    lcm
    
    """

    import math

    lcm = math.lcm(x, y)

    lcm_count = n // lcm
    x_count = n // x - lcm_count
    y_count = n // y - lcm_count

    # print(lcm_count, x_count, y_count)

    # n = 10, x_count = 6
    # 10 + 9 + 8 + 7 + 6 + 4
    k = n - x_count

    x_sum = n * (n+1) // 2 - k * (k+1) // 2

    y_sum = y_count * (y_count+1) // 2

    return x_sum - y_sum

    





    


t = int(input())
for _ in range(t):
    print(solve()) 