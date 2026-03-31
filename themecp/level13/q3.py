# https://codeforces.com/problemset/problem/1808/B

"""
logic:

"""

def total_absolute_diff(arr):
    arr.sort()
    total = 0
    n = len(arr)
    for i in range(n):
        total += arr[i] * (2 * i - n + 1)
    return total


def solve():
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    solution = 0

    # _abs = abs
    for i in range(m):
        arr = []
        for j in range(n):
            arr.append(matrix[j][i])
        
        solution += total_absolute_diff(arr)

    return solution




t = int(input())

for _ in range(t):
    print(solve())
