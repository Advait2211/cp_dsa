import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right
from math import isqrt


def solve():
    n, q = map(int, input().split())

    cb = set()

    # find factors
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            cb.add(i)
            cb.add(n//i)

    """
    rowise = []
    cur = 0

    # how much per row we can have per row
    for i in range(n, 0, -1):
        if i in cb:
            cur = n // i

        rowise.append(cur)



    

    # reverse prefix sum
    rpsum = [0] * n
    rpsum[-1] = rowise[-1]

    for i in range(n-2, -1, -1):
        rpsum[i] = rpsum[i+1] + rowise[i]
    
    """
    divs = sorted(cb, reverse=True)
    startk  = [n - d for d in divs]
    heights = [n // d for d in divs]
    m = len(divs)

    rsum = [0] * m
    acc = 0
    for j in range(m-1, -1, -1):
        end = startk[j+1] if j+1 < m else n
        acc += (end - startk[j]) * heights[j]
        rsum[j] = acc

    def rpsum(k):
        j = bisect_right(startk, k) - 1
        return rsum[j] - (k - startk[j]) * heights[j]



    # prefix sum
    # psum = [0] * n
    # psum[0] = rowise[0]

    # for i in range(1, n):
    #     psum[i] = psum[i-1] + rowise[i]

    # print(psum)



    for _ in range(q):
        a, b = map(int, input().split())

        valid = n - a

        # values greater eqt b
        sm = 0
        idx = startk[bisect_left(heights, b)]

        if idx <= valid:
            sm = a * b
            print(sm)
            # print()
            continue

        sm += (n - idx) * b


        # values smaller than b
        # idx to n - a
        frm = idx
        to = n-a
        sm += (rpsum(to) - rpsum(frm))

        
        print(sm)

            
    


t = int(input())
for _ in range(t):
    solve()