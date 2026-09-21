import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    mx = 0
    if max(a) < 0:
        return max(a)
    cur = 0
    prev = a[0]-1

    for i in range(n):
        if (a[i] - prev) % 2 == 1:
            # print("p")
            cur += a[i]
            cur = max(0, cur, a[i])
            mx = max(mx, cur)
            prev = a[i]
        else:
            # print("q")
            cur = a[i]
            mx = max(mx, cur)
            prev = a[i]

        # print(mx)


        

    return mx



    


t = int(input())
for _ in range(t):
    print(solve()) 