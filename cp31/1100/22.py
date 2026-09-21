import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    MOD = 10**9 + 7

    a = (n * (n+1) * (2 * n + 1)) // 6

    b = (n * (n + 1)) // 2

    ans = (2 * a - b) % MOD

    return (ans * 2022) % MOD
    
    


t = int(input())
for _ in range(t):
    print(solve()) 