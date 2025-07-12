# https://codeforces.com/problemset/problem/1928/B

"""
logic:

"""


def solve():
    n = int(input())
    a = list(map(int, input().split()))


    a = sorted(a)

    diff_arr = []

    for i in range(1, n):
        diff_arr.append(a[i] - a[i-1])

    # print(diff_arr)

    max_count = 0

    for i in range(len(diff_arr)-1, -1, -1):
        count = 0
        temp = 1
        for j in range(i, -1, -1):
            temp += diff_arr[j]
            if temp > n:
                break
            count += 1

        if j == 0:
            count += 1
        if count > max_count:
            max_count = count

    return max_count
        



t = int(input())

for _ in range(t):
    print(solve())
