# https://codeforces.com/problemset/problem/1836/A
"""
logic:

"""


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    thing = [0] * 101

    for val in a:
        thing[val] += 1
    
    prev_val = thing[0]

    for val in thing:
        if val > prev_val:
            return "No"
        prev_val = val

    return "Yes"


t = int(input())

for _ in range(t):
    print(solve())
