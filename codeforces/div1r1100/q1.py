import sys
import math
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(a)

    # if n % 2 == 0:
    #     p = n // 2 - 1
    #     q = n // 2
    #     median = (p + q) // 2

    #     return max(median - a[0], a[-1] - median)
    # else:
    #     median = a[n//2]
    #     return max(median - a[0], a[-1] - median)

    return math.ceil((a[-1] - a[0])/2)
        
    


t = int(input())
for _ in range(t):
    print(solve()) 