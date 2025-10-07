def solve(a, ones, zeros, flipflop):
    start, end = map(int, input().split())

    # check if possible
    length = end - start + 1

    range_ones = ones[end] - ones[start-1]
    range_zeros = zeros[end] - zeros[start-1]

    if length % 3 != 0 or range_ones % 3 != 0 or range_zeros % 3 != 0:
        return -1
    
    # now for the value calculation. 
    # if all the elements are alternate, then the cost will be 2 intially, and then a series of 1s. 
    # so even if we have 2 consecutive 0's or 1's, we can do this in elements / 3. 

    # so we just need to check if the given sequence has any consequitive values or not. 
    # i think we can compute this in the prefix sum

    if flipflop[end] - flipflop[start] > 0:
        return length // 3
    else:
        return length // 3 + 1




t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    # compute prefix sum
    ones = [0] * (n + 1)
    zeros = [0] * (n + 1)

    flipflop = [0] * (n+1)

    for i in range(1, n + 1):
        ones[i] = ones[i - 1] + (1 if a[i - 1] == 1 else 0)
        zeros[i] = zeros[i - 1] + (1 if a[i - 1] == 0 else 0)

        if i > 1 and a[i - 1] == a[i - 2]:
            flipflop[i] = flipflop[i - 1] + 1
        else:
            flipflop[i] = flipflop[i - 1]


    for _ in range(q):
        print(solve(a, ones, zeros, flipflop))