import sys
input = sys.stdin.readline

def solve():
    x, y = map(int, input().split())

    if x == y:
        if x % 2 == 1:
            return "NO"
        else:
            return "YES"
        
    x, y = max(x, y), min(x, y)

    diff = x - y

    if x % 2 == 1 and y % 2 == 1:
        return "NO"
    else:
        return "YES"
    


t = int(input())
for _ in range(t):
    print(solve()) 