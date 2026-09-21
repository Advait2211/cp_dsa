import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    prev = False

    i = 0
    while i < n and a[i] not in (1, -1):
        i += 1

    if i == n:
        print(*a)
        return

    if a[i] == -1:
        a[i] = 1

    

    j = n-1
    while j >= 0 and a[j] not in (1, -1):
        j -= 1
    
    if a[j] == -1:
        a[j] = 1 

    for p in range(i, j+1):
        if a[p] == -1:
            a[p] = 0

    print(*a)

    

    

    # for i in range(n):
    #     if a[i] == 1:
    #         prev = True

    #     if a[i] == -1:
    #         if prev:
    #             a[i] = 0
    #         else:
    #             a[i] = 1
                # prev = True

        

    


t = int(input())
for _ in range(t):
    solve()