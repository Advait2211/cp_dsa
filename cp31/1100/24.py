import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ass = sorted(a)

    for i in range(n):
        if a[i] != ass[i]:
            break


    first = a[i]

    for i in range(n):
        if a[i] != ass[i]:
            first &= a[i]


    return first




    


t = int(input())
for _ in range(t):
    print(solve()) 