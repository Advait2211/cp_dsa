def solve():
    n = int(input())
    a = list(map(int, input().split()))

    """
    what defines when a value can go to a value and when not?

    1 can go to any exp of 2
    3 can go to any multiple of 3, and would be able to find its way back
    5 can go to any place of 5 * 2k. 

    so basically we need to check if the value at every index is 2 * i k?
    k does not matter, so we just need to check if either the value should be divisble by 2 * (i) or i itself. 

    just the theory of divisibility does not matter
    any value in any position was to satisfy this equation:
    cur * (2 ** k)
    where k ranges from 0 to log2(n)

    so i suppose we first check if it is divisible by cur. 
    if yes, then check if it an exact log2 value. 
    """


    for i in range(n):
        cur = i + 1

        if a[i] < cur:
            cur, a[i] = a[i], cur

        if a[i] % cur != 0:
            return "NO"

        ratio = a[i] // cur

        if not (ratio & (ratio - 1)) == 0:
            return "NO"

    return "YES"



t = int(input())
for _ in range(t):
    print(solve())