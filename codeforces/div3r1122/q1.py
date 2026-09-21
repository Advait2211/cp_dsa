import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    return n - min(a)
    


t = int(input())
for _ in range(t):
    print(solve()) 