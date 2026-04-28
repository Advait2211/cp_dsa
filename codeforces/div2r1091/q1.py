import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    sm = sum(a)

    if sm % 2 == 1:
        return "YES"

    else:
        if n * k % 2 == 1:
            return "NO"
        else:
            return "YES"
    
    


t = int(input())
for _ in range(t):
    print(solve()) 