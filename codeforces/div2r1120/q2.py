import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())

    if k < n or k >= 2 * n:
        print(-1)
        return

    # so k will be the number of offsets

    mat = [[0] * n for _ in range(n)]

    s = set()
    val = 1

    # print(n, k)

    for i in range(n - (k - n)):
        mat[i][i] = val
        s.add(val)
        val += 1

    # print(mat)

    val = n - (k - n) + 1


    for i in range(n):
        for j in range(n):
            if mat[i][j] > 0:
                continue
            if val in s:
                while val not in s:
                    val += 1
            mat[i][j] = val
            val += 1

    for row in mat:
        print(*row)

    


t = int(input())
for _ in range(t):
    solve()