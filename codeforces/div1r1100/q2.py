import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    """
    keep the largest in the a, and then the 

    is there any case where keeping the maximum in A makes sense?
    
    """

    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]

    return sum(b) + max(a)

    


t = int(input())
for _ in range(t):
    print(solve()) 