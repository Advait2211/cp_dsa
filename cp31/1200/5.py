import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    """
    for every color. 
    we just check the max and second max frequency. 

    that's it. 

    max can be divided by two. 
    so answer will be max(maxi+1//2, smaxi)
    """

    

    
    
    


t = int(input())
for _ in range(t):
    print(solve()) 