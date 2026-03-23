import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    """
    if all are even. 
    or all are odd, then this does not work

    hmm. i thought i had this one in like seconds.
    i think i can say that this can be done by some power of two
    so i suppose just brute force powers of two could work

    but testing that would take n log n time. yeah, that works
    """

    v = 1
    maxi = 2 * max(a)

    while True:
        v *= 2
        s = set()

        for val in a:
            s.add(val % v)

        if len(s) == 2:
            break

    return v




t = int(input())
for _ in range(t):
    print(solve()) 