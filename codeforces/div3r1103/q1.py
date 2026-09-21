import sys
input = sys.stdin.readline

from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))


    # a = sorted(a, reverse=True)

    # i = 1
    # sol = a[0]
    # while i < n:
    #     if a[i] != a[i-1]:
    #         sol += a[i]
    #     else:
    #         old_i = i
    #         while i < (n-1) and a[i] == a[i+1]:
    #             i += 1

    #         if i == n-1:
    #             sol += a[i] + a[i+1]
    #         else:



    freq = Counter(a)

    a = sorted(a, reverse=True)

    # print(freq)

    max_freq = 0
    ele = -1

    for key, val in freq.items():
        if val > max_freq:
            max_freq = val
            ele = key

    if max_freq <= ((n+1) // 2):
        return sum(a)

    other = n - max_freq

    if max_freq <= other + 2:
        return sum(a)

    a2 = []

    for i in range(n):
        if a[i] != ele:
            a2.append(a[i])

    # print(a2)

    soln = sum(a2)

    soln += (len(a2) + 2) * ele

    return soln

    








    


t = int(input())
for _ in range(t):
    print(solve()) 