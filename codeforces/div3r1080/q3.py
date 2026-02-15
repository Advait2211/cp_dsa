def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # cases
    # 2 5 2 5
    # 2 5 5 2
    # 5 5 5 5
    # 2 5 4 4
    # 2 5 5 5


    prev_fix = False
    cnt = 0

    for i in range(1, n):
        if a[i] == (7 - a[i-1]) or a[i] == a[i-1]:
            if prev_fix == True:
                prev_fix = False
                continue
            cnt += 1
            prev_fix = True
            continue
        
        prev_fix = False

    return cnt
                



t = int(input())
for _ in range(t):
    print(solve())