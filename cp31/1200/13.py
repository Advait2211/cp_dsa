import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if n == m:
        return n
    
    if m == 1:
        if n == 1:
            return 1
        else:
            return 2
        
    a = sorted(a)

    diff = []

    for i in range(1, len(a)):
        diff.append(a[i] - a[i-1] - 1)

    diff.append(a[0] + n - a[-1] - 1)
    diff = sorted(diff)

    # print(diff)

    safe = 0

    f = len(diff) - 1
    m = 0

    while f >= 0 and (diff[f] - m * 4 - 1) > 0:
        diff[f] -= m * 4 + 1
        safe += diff[f]

        m += 1
        f -= 1

    if f >= 0 and diff[f] - m * 4 > 0:
        safe += 1
    
        

    return n - safe

    

    
    


t = int(input())
for _ in range(t):
    print(solve()) 