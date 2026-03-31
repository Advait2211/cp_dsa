import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 2:
        print(a[0], a[0], end=" ")
        return

    a = sorted(a, reverse=True)
    # print(a)
    """
    3 4 4 5 5
    3 3 3 3 4 4 4 4 4 5

    3 - 4
    4 - 5
    5 - 1

    smallest element will have (n-1)
    second smallest will have (n-2)
    third smallest will have (n-3)
    and so on

    okay so i was dumb to try to figure it out from just freq. 
    it would be much simpler to get it done using using both the array and the freq. 

    for 4 elements:
    1 2 3 4
    1 1 1 2 2 3


    0 1 3 6 10 

    """

    idx = 0
    op = 1

    while idx < len(a):
        print(a[idx], end = " ")
        idx = idx + op
        op += 1

    op -= 1

    while op < n:
        print(max(a), end = " ")
        op += 1


    


t = int(input())
for _ in range(t):
    solve()
    print()