import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    b = [-2] * n

    # left sweep

    for i in range(n):
        if a[i] == 0:
            b[i] = 1
        elif a[i] > 0:
            b[i] = 2
            if i - a[i] >= 0:
                b[i-a[i]] = max(b[i-a[i]], 1)
            if i + a[i] < n:
                b[i+a[i]] = max(1, b[i+a[i]])

    for i in range(n):
        if b[i] in (2, -2):
            b[i]=0


    # take prefix sum to check if 


    # first pass - remove if invalid

    for i in range(a):
        if a[i] > 0:

        

    print(b)

    


t = int(input())
for _ in range(t):
    print(solve()) 