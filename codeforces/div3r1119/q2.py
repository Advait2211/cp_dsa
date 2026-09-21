import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    first = 0
    second = 0
    third = 0
    fourth = 0

    for val in a:
        if val % 4 == 0:
            first += 1
        elif val % 4 == 1:
            second += 1
        elif val % 4 == 2:
            third += 1
        else:
            fourth += 1
        

    return max(first, second, third, fourth, second+fourth)


    


t = int(input())
for _ in range(t):
    print(solve()) 