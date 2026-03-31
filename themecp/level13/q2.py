# https://codeforces.com/problemset/problem/1784/A

"""
logic:

"""


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(a)

    # arr = []

    # for i in range(1, to+1):
    #     arr.append(i)

    solution = 0

    first = a[0]
    if first == 1:
        pass
    else:
        solution += first - 1
        a[0] = 1

    for i in range(1, n):
        # if a[i] == a[i-1]:
        #     pass
        # elif a[i] == a[i-1] + 1:
        #     pass
        if a[i] > a[i-1] + 1:
            solution += a[i] - (a[i-1] + 1)
            a[i] = a[i-1]+1

    return solution


t = int(input())

for _ in range(t):
    print(solve())
