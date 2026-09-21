import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    # x, y, z = map(int, input().split())

    """
    impact is higher if we remove a lower cube
    if we remove first cube, then all have to move, which is maximum impact
    so obviously we check from the right side

    can we compute impact faster than O(n)

    we can just copy a dictionary right?
    a freq dict?

    whereever there is a SINGLE GAP
    all of that grade will move
    """

    

    sufmin = [n + 1] * n
    for i in range(n - 2, -1, -1):
        sufmin[i] = min(sufmin[i+1], a[i+1])

    # print(sufmin)

    can_move = 0
    for i in range(n):
        trapped = min(a[i], sufmin[i])
        can_move += (a[i] - trapped)


    freq = defaultdict(int)
    max_gain = 0
    

    for i in range(n):
        gain = -1 
        if a[i] <= sufmin[i]:
            gain += 1
        gain += freq[a[i]]

        # print(gain)
        
        if gain > max_gain:
            max_gain = gain
        
        if a[i] >= sufmin[i]:
            freq[sufmin[i]] += 1

        # print(freq)

    print(freq)


    return can_move + max_gain


    


t = int(input())
for _ in range(t):
    print(solve()) 