import sys
input = sys.stdin.readline

def solve():
    v = int(input())
    verts = list(map(int, input().split()))

    d = int(input())
    dams = list(map(int, input().split()))

    """
    we will always need d-1 cameras

    can we just remove the last camera? - same branch would not be able to identify

    but the first one on that branch we can remove


    """
    print(d-1, end = " ")
    print(*dams[1:])

    


t = int(input())
for _ in range(t):
    solve()