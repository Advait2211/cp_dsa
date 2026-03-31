import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    z = []

    for i in range(n):
        z.append(y[i]-x[i])

    """
    we have to use minimum elements to make groups total>=0.
    but the minimum group size is 2. 

    what if we just use a two pointer approach?
    nah, dp would be better ig?

    two pointer should work as the number of elements used does not matter. only the number of groups.
    so we can basically utilise the largest positive - largest smaller negative

    the key point being: it makes no sense to make a group of size larger than 2. 
    """

    z = sorted(z)

    # print(z)
    l = 0
    r = n-1

    pairs = 0

    while l < r:
        if z[l] + z[r] >= 0:
            pairs += 1
            r -= 1
            l += 1
        else:
            l += 1

    return pairs



    


t = int(input())
for _ in range(t):
    print(solve()) 