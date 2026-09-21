import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    """
    very easy actually
    only 2 possible minimum values
    smallest num even -> make all that
    smallest num odd -> check that value, and val + 1

    oh the smart case here is that it is not necessary that values will always decompose to that value
    take 8 and 9
    minimum would be like
    4 5
    4 3
    2 3
    2 4
    2 2

    can we make an assumption that all values have to come down to 2 ?
    
    """
    
    mini = min(a)

    if mini % 2 == 0:




t = int(input())
for _ in range(t):
    print(solve()) 