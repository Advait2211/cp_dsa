import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    p = int(input())
    p -= 1

    """
    special index must be in every query
    this means that whatever is the value of the special index
    should be the value of the array

    we count islands
    0 islands and 1 islands

    like in 010101

    3 zero islands
    3 one islands

    010101
    101011

    if both require the same operations, then we obviously want to make everything equal to a[p-1]

    else we just make all nodes the opposite
    and then flip

    can we say that
    at every move, we can remove 2 islands?
    """

    if len(set(a)) == 1:
        return 0


    l, r = 1, 1

    for i in range(1, p):
        l += abs(a[i] - a[i-1])

    for i in range(p+1, n):
        r += abs(a[i] - a[i-1])

    to_make = a[p]

    if p > 0 and a[p] == a[p-1]:
        l = max(0, l-1)
    
    if p < (n-1) and a[p] == a[p+1]:
        r = max(0, r-1)

    if a[0] == to_make:
        l = max(0, l-1)
    
    if a[-1] == to_make:
        r = max(0, r-1)

    # print(l, r)
    return max(r, l) + max(r, l) % 2


    

    


t = int(input())
for _ in range(t):
    print(solve())