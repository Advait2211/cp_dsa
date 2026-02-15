def solve():
    n = int(input())
    a = [1] * n

    for i in range(n-1):
        c = int(input())

        a[c] += 1
        

    val = max(a)
    sol = []
    print(a)

    # i is the number of partitions
    # j = n // i is the number of nodes
    for i in range(1, n+1):
        # if divisible by i, then go ahead
        if n % i == 0:
            j = n // i
            # check if after partition, we can still work with it. 

            # we just need to check if we can split the array into equal value pieces

            sol.append(i)
    
    print(*sol)



t = 1
for _ in range(t):
    solve()