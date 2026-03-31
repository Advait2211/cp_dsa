import sys
input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    suma = sum(a)

    update = -1
    gupdate = -1
    updatedAt = [-1] * n
    newVal = list(a)
    prev_sum = suma

    for i in range(q):
        b = list(map(int, input().split()))
        if b[0] == 2:
            update = i
            prev_sum = n * b[1]
            gupdate = b[1]
            print(prev_sum)

        else:
            idx, val = b[1], b[2]
            if update > updatedAt[idx-1]:
                # print(1)
                prev_sum += val - gupdate
                # print(prev_sum)
                newVal[idx-1] = val
                updatedAt[idx-1] = i
            else:
                # print(2)
                prev_sum += val - newVal[idx-1]
                newVal[idx-1] = val
                updatedAt[idx-1] = i

            print(prev_sum)




    


t = 1
for _ in range(t):
    solve()