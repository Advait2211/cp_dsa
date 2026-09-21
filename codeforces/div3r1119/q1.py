import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = input()

    cnt = 0
    seg = False

    for i in range(n):
        if a[i] == '0':
            seg = True

        if (i+1) % k == 0:
            # print(i)
            if seg:
                seg = False
            else:
                cnt += 1
        

    return cnt



    


t = int(input())
for _ in range(t):
    print(solve()) 