import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(1, n):
        if abs(a[i] - a[i-1]) == 1:
            ans += 1
        else:
            diff = abs(a[i] - a[i-1])
            if a[i] % diff == 0:
                ans += 1


    return ans
    


t = int(input())
for _ in range(t):
    print(solve()) 