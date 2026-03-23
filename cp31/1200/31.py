import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(a)

    """
    can we just break the question into 3 sets
    even even
    even odd
    odd odd 

    no
    because 01 & 10 = 0  < 01 XOR 10 = 11
    and.    10 & 11 = 10 > 10 XOR 11 = 1

    what other information could we have to deduce general results?
    comparing results from say between 4 - 8 and 2 - 4, would always have this pattern
    AND would always losing the leading digit, while XOR will always introduce that digit. 
    therefore i can say for sure that AND will always be less than XOR. 
    but what about elements in the same space?

    ah, the first one will get cancelled, therefore they will always be greater. 
    so we just need to find how many numbers are between each 2's power ranges
    and then nC2.

    """

    vals = []

    import math
    prev = math.floor(math.log2(a[0]))
    cnt = 0
    for v in a:
        cur = math.floor(math.log2(v))
        # print(cur, prev)
        if cur != prev:
            vals.append(cnt)
            cnt = 0
        cnt += 1
        prev = cur
    
    vals.append(cnt)

    soln = 0
    for val in vals:
        soln += val * (val-1) // 2

    return(soln)

    


t = int(input())
for _ in range(t):
    print(solve()) 