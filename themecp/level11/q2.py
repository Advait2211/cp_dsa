import sys
input = sys.stdin.readline

def solve():
    x1, x2, y1, y2 = map(int, input().split())

    """
    potential games:
    x1 y1
    x1 y2
    x2 y1
    x2 y2

    and just check how many times x wins.
    """

    count = 0

    if (x1 > y1 and x2 > y2) or (x1 == y1 and x2 > y2) or (x1 > y1 and x2 == y2):
        count += 2
    if (x1 > y2 and x2 > y1) or (x1 == y2 and x2 > y1) or (x1 > y2 and x2 == y1):
        count += 2

    return count
    


t = int(input())
for _ in range(t):
    print(solve()) 