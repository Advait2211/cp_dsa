import sys
input = sys.stdin.readline

def solve():
    a, b, c = map(int, input().split())

    # if b > a:
    #     return b - a
    # else:
    #     return a+ c - b

    return max(a+c - b, b - a)
    


t = int(input())
for _ in range(t):
    print(solve()) 