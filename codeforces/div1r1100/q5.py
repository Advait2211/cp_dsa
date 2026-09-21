import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    f = a + b

    a = sorted(a)
    b = sorted(b)

    if n % 2 == 1:
        ma = a[n//2]
        mb = b[n//2]
    else:
        ma = a[n//2-1]
        mb = a[n//2-1]

    return min(ma, mb)

    f = sorted(f)
    # print(f)

    return(f[len(f)//2-1])
    


t = int(input())
for _ in range(t):
    print(solve()) 
    print()