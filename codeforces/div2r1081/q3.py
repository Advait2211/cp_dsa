def solve():
    n, h, k = map(int, input().split())
    h2 = int(h)
    a = list(map(int, input().split()))

    """
    1 objectives:
    minimise time
    2 constraints
    reload time, minimise shots fired

    when can we afford an reload? only when over time it cover not being shot by immediately
    every round is going to deal the same amount of damage

    this means, only the last round depends on the reload
    oh so essentially reload just does not matter. 
    because at the end of every round, you are going to deal the same amount of damage anyways. 
    so it is logical, to swap the maximum gain points

    so we have to make the maximum gain swap

    how to decide maximum gain swap?
    say you have this
    4 2 3 5 3

    replacing 4 and 5 gives you a gain of 1
    replacing 2 and 5 gives you a gain of 3 - the later the gain comes from, the better. so ideally we would swap the largest last element with the smallest first element

    health % (sum of points in the row) = points to be removed in the last itr

    so basically we need to found out a psum to be greater than atleast k
    
    the max you can save is one second anyways
    wait this is wrong
    you can save more than one second
    this can be computed by just how much gain you can have

    so we need a two pointer kind of approach
    """

    asum = sum(a)

    last = h % asum

    if last == 0:
        return n * (h//asum) + k * ((h//asum)-1)

    # print(last)


    psum = [0] * (n + 1)
    for i in range(n):
        psum[i+1] = psum[i] + a[i]
    
    # prefix array to find smallest val to the point
    pref_min = [0] * n
    pref_min[0] = a[0]
    for i in range(1, n):
        pref_min[i] = min(pref_min[i-1], a[i])

    # prefix array to find largest val to the point
    pref_max = [0] * n
    pref_max[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        pref_max[i] = max(pref_max[i+1], a[i])

    

    extra = -1
    for i in range(n):
        s = psum[i+1]

        if s >= last:
            extra = i+1
            break

        if i+1 < n:
            gain = pref_max[i+1] - pref_min[i]
            if s + gain >= last:
                extra = i+1
                break

    # answer would be initial + reload + extra
    itr = (h//asum)
    initial = n * itr
    reload = k * itr


    # print(f"{itr=}")
    # print(f"{h=}")
    # print(f"{asum=}")
    # print(f"{initial=}")
    # print(f"{reload=}")
    # print(f"{extra=}")
    # print(f"{n=}")
    return initial + reload + extra



    



t = int(input())
for _ in range(t):
    print(solve())
    # print()