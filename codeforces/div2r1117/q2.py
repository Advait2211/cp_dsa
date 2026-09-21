import sys
input = sys.stdin.readline

def solve():
    m, n = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # b.reverse()
    # print(b)

    asm = a[-1]
    bsm = b[-1]

    for i in range(m-1):
        asm += a[i] - a[i+1] + 1

    for i in range(n-1):
        bsm += b[i] - b[i+1] + 1
        # print(bsm)
        

    # print(asm, bsm)

    if asm >= bsm:
        return 1

    elif bsm > asm:
        return 2

    return 1.5


    


t = int(input())
for _ in range(t):
    print(solve()) 