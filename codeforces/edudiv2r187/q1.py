def solve():
    n, m, d = map(int, input().split())

    total_weight = n * m

    # how would the weight decrease
    # n-1 * m
    towers = 1
    cur_weight = 0

    for i in range(1, n):
        cur_weight += m
        if cur_weight > d:
            towers += 1
            cur_weight = 0

    return towers




t = int(input())
for _ in range(t):
    print(solve())