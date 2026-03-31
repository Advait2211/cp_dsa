import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if a[-2] > a[-1]:
        print(-1)
        return
    
    

    if a[-1] < 0 and a[-2] < 0:
        if sorted(a) == a:
            print(0)
        else:
            print(-1)
    else:
        print(n-2)
        for i in range(n-2):
            print(i+1, n-1, n)
            a[i] = a[-2] - a[-1]

    

    # print(a)

    


    


t = int(input())
for _ in range(t):
    solve()