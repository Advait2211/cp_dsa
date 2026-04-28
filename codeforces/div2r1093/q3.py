import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    x, y, z = map(int, input().split())

    """
    what does it mean from the context of the problem that one element has repeated thrice

    there are say these queries:

    1 - k
    k - x

    what is the largest possible segment that satisfies this condition:
    len(query) = output
    - n
    
    """
    


t = int(input())
for _ in range(t):
    print(solve()) 