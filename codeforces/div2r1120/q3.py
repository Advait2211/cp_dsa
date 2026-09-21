import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    notass = [0] * (n+1)


    for i in range(n):
        idx = i + 1

        start = min(idx * a[i], n)
        end = min(idx * (a[i] + 1), n)

        notass[start] += 1
        notass[end] -= 1

    # print(notass)

    sm = 0

    for i in range(n+1):
        sm += notass[i]

        notass[i] = sm

    # print(notass)

    soln = []

    for i in range(n):
        if notass[i] > 0:
            continue
        soln.append(i)

    print(len(soln))
    print(*soln)



    


t = int(input())
for _ in range(t):
    solve()