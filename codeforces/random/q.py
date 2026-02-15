def solve():
    n = int(input())
    a = list(map(int, input().split()))

    distinct = set(a)
    k = len(distinct)

    ans = float('inf')

    for val in distinct:
        if val >= k:
            ans = min(ans, val)

    return(ans)




t = int(input())
for _ in range(t):
    print(solve())