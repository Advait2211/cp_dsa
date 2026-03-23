import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    it = 0

    for i in range(1, n):
        it += abs(a[i] - a[i-1])

    if it == 0:
        return 1

    switch = 0
    dir = ''

    # if a[1] > a[0]:
    #     dir = 'up'
    # elif a[1] < a[0]:
    #     dir = 'down'
    # else:
    #     dir = 0

    

    for i in range(1, n):
        if a[i] > a[i-1]: # uphill
            if dir != 'up':
                switch += 1
            dir = 'up'
        elif a[i] < a[i-1]: # downhill
            if dir != 'down':
                switch += 1
            dir = 'down'

        # print(f"{switch=}")

    return switch+1

    


t = int(input())
for _ in range(t):
    print(solve()) 