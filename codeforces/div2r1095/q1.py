import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # if 0 in a:
    #     return 0
    # f = 0

    # if 1 in a:
    #     f = a.count(1)

    ans = 0

    for val in a:
        if val == 0:
            return 0
        elif val == 1:
            pass
        else:
            ans += val

        
    if a[-1] == 1:
        ans += 1

    return ans


    # return max((sum(a) - f) % 676767677, 1)

    


t = int(input())
for _ in range(t):
    print(solve())