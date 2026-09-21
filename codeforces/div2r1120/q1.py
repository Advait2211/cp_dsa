import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    one = a.count(1)
    zero = a.count(0)

    if zero > one:
        return "Elsie"
    else:
        return "Bessie"
    


t = int(input())
for _ in range(t):
    print(solve()) 