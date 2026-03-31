import sys
input = sys.stdin.readline

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    # mini = min(a)
    total = 0

    """
    so basically we sort
    basically extra cost per iteration is the number of elements
    and over time when an element is unreachable, the cost of iteration will become (n-1)
    and so on. 

    we repeat this

    we check each element. 
    we would have x amount of tokens exhausted before reaching that element. 
    so we just need to find how many times that element can be used. 

    so some formula like:
    x - used = k
    till what value of k can you keep on accepting. 
    the natural cap would be something like

    (x - (cost of a + cost of b)) // 2 
    this is the amount of times you can buy the sugar on that point
    maybe the same for c

    x - (ca + cb + cc) // 3

    """

    a = sorted(a)
    res = 0
    psum = 0
    for i in range(n):
        psum += a[i]
        res += max(0, (x - psum) // (i+1) + 1)
        
        # print(f"{psum=}")
        # print(f"{res=}")
        



    return res


    
    


t = int(input())
for _ in range(t):
    print(solve()) 