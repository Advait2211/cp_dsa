def solve():
    n = int(input())
    a = list(map(int, input().split()))

    seta = set(a)

    a = [float('inf')] * (n+1)
    # if 1 in seta:
    #     a[1] = 1
    #     seta.remove(1)


    for x in seta:
        a[x] = 1

    for i in range(2, n + 1):
        for item in seta:
            if item > i:
                continue
            if i % item == 0:
                val = i // item

                if a[val] != float('inf'):
                    a[i] = min(a[i], a[val] + 1)


    for i in range(1, n + 1):

        if a[i] == float('inf'):
            print("-1", end=" ")
        else:
            print(a[i], end=" ")

    
    



t = int(input())
for _ in range(t):
    solve()
    print()