import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    suma = sum(a)
    if suma < k:
        return -1
    if suma == k:
        return 0
    
    """
    0101011100

    hmm
    bibibop

    what to do
    i think we can just make bunches of ones and bunches of zeros

    so this 9 3
    0 1 0 1 1 1 0 0 1
    
    -1 1 -1 3 -2 1

    there is an even more optimal way to think about this
    i am thinking in the wrong direction

    what are the possibilities:
    you can have either 0 or 1 at the end. 

    if 1 is present, then taking that 1 is obviously the default choice

    say now both have 0. 
    then we need to find which one is the optimal 0 for us to delete to reach one. 

    we could use the closest 1 metric. but this is not optimal.

    then what could be optimal ? 

    i why do i end up understanding the wrong question. 

    we want to find the largest subarray whos sum equals k

    subarray sum equals k. 

    so what if we take prefix sum
    and then from each point 
    how many elements would we have to delete to reach this solution

    what would the formula for that look like?
    k is the target

    starting from the specific idx
    n - psum[idx]
    (remove everything that is not counted in the idx)

    and then check what is the farthest element till which we can use the solution
    so we want to find the rightmost element which can get it done


    oh. so sliding window. and we want to have the window of the largest size. 

    so l = 0, and r initially will the farthest element till which the largest value can be 

    """

    # psum = [0] * (n+1)

    # for i in range(n):
    #     psum[i+1] = psum[i] + a[i]

    # print(psum)

    # maxlen = 0

    # for i in range(len(psum)):


    l = 0
    r = 0
    psum = 0
    # init loop
    for i in range(n):
        psum += a[i]
        if psum == k:
            break

    r = i

    mwin = (r - l + 1)

    # print(l, r)

    while r < n-1:
        r += 1
        if a[r] == 1:
            while a[l] == 0:
                l += 1
            l += 1

        mwin = max(mwin, r - l + 1)
        # print(f"{mwin=}")

    return n - mwin




    



    
    


t = int(input())
for _ in range(t):
    print(solve()) 
    # print()