import sys
import bisect
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)

    def reachable(mex):
        reach = []
        past = set()
 
        for val in a:
            if val < mex and val not in past:
                past.add(val)
            else:
                reach.append(val)
        



        idx = 0
        for i in range(mex):
            if i not in past:

                while idx < len(reach) and reach[idx] < 2 * i + 1:
                    idx += 1

                if idx == len(reach):
                    return False
                idx += 1
        return True






    # smh
    # this is binary search
    # answer can be reached after a point

    l = 0
    r = n
    mex = 0


    while l <= r:
        mid = (l+r)//2

        if reachable(mid):
            mex = mid
            l = mid + 1
        else:
            r = mid - 1
                    
    return mex

t = int(input())
for _ in range(t):
    print(solve())