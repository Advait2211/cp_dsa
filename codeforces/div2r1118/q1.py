import sys
input = sys.stdin.readline
import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    return math.gcd(a[0], a[-1])
    


t = int(input())
for _ in range(t):
    print(solve()) 